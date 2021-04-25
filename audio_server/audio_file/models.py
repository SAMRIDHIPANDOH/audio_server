from django.db import models
from django.core.exceptions import ValidationError
from django import forms
from django.utils.timezone import now
from datetime import date,datetime,timezone
from django.contrib.postgres.fields import ArrayField
def validate_date(value):
    return 

class song(models.Model):
    name =models.CharField(max_length=100)
    duration=models.PositiveIntegerField(default=0)
    upload_time=models.DateTimeField(default=datetime.now())

class podcast(models.Model):
    name =models.CharField(max_length=100)
    duration=models.PositiveIntegerField(default=0)
    upload_time=models.DateTimeField(default=datetime.now())
    host=models.CharField(max_length=100)
    participants=ArrayField((models.CharField(max_length=100)),size=10,blank=True)


class audiobook(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    narrator=models.CharField(max_length=100)
    duration=models.PositiveIntegerField(default=0)
    upload_time=models.DateTimeField(default=datetime.now())

class audioType(models.Model):
    type=models.CharField(max_length=100)
