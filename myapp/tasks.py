from celery import shared_task
from celery.schedules import crontab
from .models import Counter
import logging

logger = logging.getLogger(__name__)

@shared_task
def daily_message():
    print("Daily reminder: It's 2 PM!")


# count after 1 minute

@shared_task
def count_after_1_minute():
    logger.info("Starting count task")
    try:
        counter = Counter.objects.first()  # Fetch the first counter object
        if counter:
            counter.count += 1
            counter.save()
            logger.info(f"Count updated: {counter.count}")
        else:
            logger.warning("No counter found!")
    except Exception as e:
        logger.error(f"Error in count_after_1_minute task: {e}")
