from django.db import models
from django.contrib.auth.models import User

class Header(models.Model):
    highlight_type = models.TextField()
    habit_name = models.CharField(max_length=255)
    tracking_name = models.CharField(max_length=255)

class Journal(models.Model):
    highlight_text = models.TextField()
    is_habit_practiced = models.BooleanField()
    tracking_value = models.FloatField()
class Goal(models.Model):
    name = models.CharField(max_length=255)
    is_done = models.BooleanField()
