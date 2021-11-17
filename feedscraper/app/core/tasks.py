from app.celery import app
from celery import shared_task
import json
import requests
from bs4 import BeautifulSoup
from time import sleep
from datetime import datetime # for time stamps

from core.models import News

headers = {
    'referer':'https://mail.google.com/',
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}

@app.task
def scrape_aapl():

    url = 'https://feeds.finance.yahoo.com/rss/2.0/headline?s=AAPL&region=US&lang=en-US'
    symbol = 'AAPL'

    scrape_feed(url, symbol)


@app.task
def scrape_twtr():

    url = 'https://feeds.finance.yahoo.com/rss/2.0/headline?s=TWTR&region=US&lang=en-US'
    symbol = 'TWTR'

    scrape_feed(url, symbol)

@app.task
def scrape_intc():

    url = 'https://feeds.finance.yahoo.com/rss/2.0/headline?s=TWTR&region=US&lang=en-US'
    symbol = 'INTC'

    scrape_feed(url, symbol)

@app.task
def scrape_gc_gold():

    url = 'https://feeds.finance.yahoo.com/rss/2.0/headline?s=GC%3DF&region=US&lang=en-US'
    symbol = 'GC=F'

    scrape_feed(url, symbol)

@app.task
def scrape_feed(_url, _symbol):
    try:
        print('Starting rss feed scrape for symbol %s!'%_symbol)
        req = requests.get(
            url=_url,
            headers=headers
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
        print('The scraping job for {_symbol} failed. See exception : ')
        print(ex)
            



    