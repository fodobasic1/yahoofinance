from datetime import timezone
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

app = Celery('app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.enable_utc=False
app.conf.update(timezone='CET')

app.conf.beat_schedule = {
    'Scrape RSS Feed Symbol AAPL': {
        'task': 'core.tasks.scrape_aapl',
        'schedule': crontab(minute='*/1')
    },
    'Scrape RSS Feed Symbol TWTR': {
       'task': 'core.tasks.scrape_twtr',
       'schedule': crontab(minute='*/1')
    },
    'Scrape RSS Feed Symbol GC_GOLD': {
       'task': 'core.tasks.scrape_gc_gold',
       'schedule': crontab(minute='*/1')
    },
    'Scrape RSS Feed Symbol INTC': {
       'task': 'core.tasks.scrape_intc',
       'schedule': crontab(minute='*/1')
    }
}

app.autodiscover_tasks()