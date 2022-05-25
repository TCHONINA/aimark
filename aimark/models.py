from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Mark(models.Model):
    name = models.CharField(max_length=100, null=False)
    image = models.ImageField(max_length=100, null=False,upload_to='images/')
    created_at = models.DateField(default=datetime.now,null=False)

    def __str__(self):
        return self.name


class Point(models.Model):
    mark = models.ForeignKey(Mark,related_name='points', on_delete=models.CASCADE)
    num = models.IntegerField(null=False,default=1)
    x = models.FloatField(null=False)
    y = models.FloatField(null=False)
