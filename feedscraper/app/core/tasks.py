from app.celery import app
from core.models import News
from django.conf import settings
from core.helper import build_query_from_symbol

import requests
from bs4 import BeautifulSoup
from time import sleep
from datetime import datetime 

# Task for scraping RSS for symbol AAPL
@app.task
def scrape_aapl():

    symbol = 'AAPL'

    scrape_feed(symbol)

# Task for scraping RSS for symbol TWTR
@app.task
def scrape_twtr():

    symbol = 'TWTR'

    scrape_feed(symbol)

# Task for scraping RSS for symbol INTC
@app.task
def scrape_intc():

    symbol = 'INTC'

    scrape_feed(symbol)

# Task for scraping RSS for symbol GC=F
@app.task
def scrape_gc_gold():

    symbol = 'GC=F'

    scrape_feed(symbol)

# Root function for scraping feed with input parameter 'symbol',
# which reprents for which symbol is scraping going to be done [AAPL, TWTR, GC=F, INTC].

# Function calls helper method for building query, creates request and calls GET with that URL
# BeautifulSoup will pull data from recieved XML

# UPSERT - because tasks are running periodically, sometimes same articles might be pulled - or at least same GUID
# if that GUID already exists - update other fields. If not - create new object 
@app.task
def scrape_feed(_symbol):
    try:
        print('Starting rss feed scrape for symbol %s!'%_symbol)
        _url = build_query_from_symbol(_symbol)
        req = requests.get(
            url = _url,
            headers = settings.HEADERS
        )
        soup = BeautifulSoup(req.content, features='xml')

        articles = soup.find_all('item')

        for item in articles:

            _guid = item.find('guid').text

            if News.objects.filter(guid = _guid).exists():
                News.objects.filter(guid = _guid).update(
                    description = item.find('description').text,
                    link = item.find('link').text,
                    publishedDate = datetime.strptime(item.find('pubDate').text, '%a, %d %b %Y %H:%M:%S %z'),
                    title = item.find('title').text,
                )
            else:
                News.objects.create(
                    description = item.find('description').text,
                    guid = item.find('guid').text,
                    link = item.find('link').text,
                    publishedDate = datetime.strptime(item.find('pubDate').text, '%a, %d %b %Y %H:%M:%S %z'),
                    title = item.find('title').text,
                    symbol = _symbol
                )

            sleep(3)

    except Exception as ex:
        print('The scraping job for %s failed. See exception : '%_symbol)
        print(ex)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
            



    