# Yahoo Finance Scraper

Yahoo Finance Scraper is Django based REST API Service for financial news.
It has two parts : 
 - Scraping Service 
 - REST Api
  
The Scraping Service uses Yahoo Finance RSS feed for fetching data. It is collecting data for four symbols :
- [APPL](https://feeds.finance.yahoo.com/rss/2.0/headline?s=AAPL&region=US&lang=en-US)
- [TWTR](https://feeds.finance.yahoo.com/rss/2.0/headline?s=TWTR&region=US&lang=en-US)
- [INTC](https://feeds.finance.yahoo.com/rss/2.0/headline?s=INTC&region=US&lang=en-US)
- [GC=F](https://feeds.finance.yahoo.com/rss/2.0/headline?s=GC%3DF&region=US&lang=en-US)

The second part is used to retrieve collected data from Yahoo Finance RSS. 

## Tech

Technologies used :

- Django Framework
- PostgreSQL
- Celery Beat
- Redis

## Running the app

Yahoo Finance Scraper requires to have following on your local machine :
- [Docker](https://www.docker.com/) v20.10
- [Docker Compose](https://docs.docker.com/compose/install/) v1.29.2
- [Python](https://www.python.org/downloads/) v3

Clone this [repository](https://github.com/fodobasic1/yahoofinance.git)
```sh
git clone https://github.com/fodobasic1/yahoofinance.git
```

Navigate into root of the app
```sh
yourFolder\yahoofinance\feedscraper\
```
and run docker-compose command
```sh
docker-compose up --build
```

After successful aggregation the output of each container you are abble to retrieve the data via API 
```sh
curl -XGET -H "Content-type: application/json" 'http://localhost:8000/news'
curl -XGET -H "Content-type: application/json" 'http://localhost:8000/news/<NewsGUID>'
```

