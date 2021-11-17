from app.celery import app
from core.models import News

import requests
from bs4 import BeautifulSoup
from time import sleep
from datetime import datetime 


headers = {
    'referer':'https://mail.google.com/',
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
}

@app.task
def scrape_aapl():

    url = 'https://feeds.finance.yahoo.com/rss/2.0/headline?s=AAPL&region=US&lang=en-US'
    symbol = 'AAPL'

    try:
        print('Starting rss feed scrape for symbol %s!'%symbol)
        req = requests.get(
            url=url,
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
                    symbol = symbol
                )

            sleep(3)

    except Exception as ex:
        print('The scraping job for %s failed. See exception : '%symbol)
        print(ex)


@app.task
def scrape_twtr():

    url = 'https://feeds.finance.yahoo.com/rss/2.0/headline?s=TWTR&region=US&lang=en-US'
    symbol = 'TWTR'

    try:
        print('Starting rss feed scrape for symbol %s!'%symbol)
        req = requests.get(
            url=url,
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
                    symbol = symbol
                )

            sleep(3)

    except Exception as ex:
        print('The scraping job for %s failed. See exception : '%symbol)
        print(ex)


@app.task
def scrape_intc():

    url = 'https://feeds.finance.yahoo.com/rss/2.0/headline?s=TWTR&region=US&lang=en-US'
    symbol = 'INTC'

    try:
        print('Starting rss feed scrape for symbol %s!'%symbol)
        req = requests.get(
            url=url,
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
                    symbol = symbol
                )

            sleep(3)

    except Exception as ex:
        print('The scraping job for %s failed. See exception : '%symbol)
        print(ex)


@app.task
def scrape_gc_gold():

    url = 'https://feeds.finance.yahoo.com/rss/2.0/headline?s=GC%3DF&region=US&lang=en-US'
    symbol = 'GC=F'

    try:
        print('Starting rss feed scrape for symbol %s!'%symbol)
        req = requests.get(
            url=url,
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
                    symbol = symbol
                )

            sleep(3)

    except Exception as ex:
        print('The scraping job for %s failed. See exception : '%symbol)
        print(ex)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
            



    