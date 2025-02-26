from celery import shared_task
from celery.schedules import crontab
from .models import Counter

@shared_task
def daily_message():
    print("Daily reminder: It's 2 PM!")


# count after 1 minute

@shared_task
def count_after_1_minute():
    print('counting task')
    counter = Counter.objects.first()
    counter.count += 1
    counter.save()
    print('count ', counter)
