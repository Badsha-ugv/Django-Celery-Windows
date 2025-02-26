from celery import shared_task
from celery.schedules import crontab

@shared_task
def daily_message():
    print("Daily reminder: It's 2 PM!")