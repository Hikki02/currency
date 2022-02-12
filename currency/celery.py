import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ADI.settings')

app = Celery('ADI')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'every-day': {
        'task': 'users.tasks.send_a_currency_notification',
        'schedule': crontab(hour=12, minute=0)
    }
}
app.autodiscover_tasks()
