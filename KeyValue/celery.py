import os
from celery import Celery
from django.conf import settings
# setting the Django settings module.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'KeyValue.settings')
app = Celery('KeyValue',broker=settings.CELERY_BROKER_URL)
app.config_from_object('django.conf:settings')

# Looks up for task modules in Django applications and loads them
app.autodiscover_tasks()

app.conf.beat_schedule = {
      'add-every-1-minute': {
        'task': 'app.tasks.delete_ttl_obj',
        'schedule': 60,
    },
}
