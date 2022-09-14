from celery import shared_task
from django.utils import timezone
from .models import Store

@shared_task
def delete_ttl_obj():
    k = Store.objects.filter(created_at__lte=timezone.now().time()).delete()
    print(k,'delete objs')