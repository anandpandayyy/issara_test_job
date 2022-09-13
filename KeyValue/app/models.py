from django.db import models
from datetime import datetime,timedelta
# Create your models here.
class Store(models.Model):
    key = models.CharField(max_length=100,unique=True)
    value = models.CharField(max_length=100)
    created_at = models.TimeField(null=True,blank=True)
    
    def save(self, *args, **kwargs):
        self.created_at = datetime.now()+timedelta(minutes=5)
        super(Store, self).save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.key}-{self.value}-{self.created_at}'
    
    @classmethod
    def delete_old_records(cls):
        cut_off = datetime.datetime.now() - datetime.timedelta(minutes=minutes)
        cls.objects.filter(created__lt=cut_off).delete()