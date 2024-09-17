from __future__ import absolute_import, unicode_literals
import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'currency_converter.settings')

app = Celery('currency_converter')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'exchange_rates': {
        'task': 'conversion.tasks.get_exchange_rates',
        'schedule': 15,
    },
}
app.conf.timezone = 'Asia/Baku'