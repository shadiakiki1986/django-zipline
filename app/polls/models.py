from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class Order(models.Model):
    order_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.order_text
    def was_published_recently(self):
        now = timezone.now()
        return now >= self.pub_date >= now - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Fill(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    fill_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.fill_text
