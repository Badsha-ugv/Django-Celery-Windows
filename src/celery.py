from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')

app = Celery('src')

# Use Redis as the broker
app.config_from_object('django.conf:settings', namespace='CELERY')


from celery.schedules import crontab


# Load tasks from all registered Django apps
app.autodiscover_tasks()

# Add this to settings.py
app.conf.beat_schedule = {
    # 'daily-2pm-task': {
    #     'task': 'myapp.tasks.daily_message',
    #     # 'schedule': crontab(hour=14, minute=54),  # 2 PM UTC
    #     'schedule': crontab(),  # 2 PM UTC
    # },
    'count_every_minute': {
        'task': 'myapp.tasks.count_after_1_minute',
        # 'schedule': crontab(hour=14, minute=54),  # 2 PM UTC
        'schedule': crontab(minute='2'),
    },
}