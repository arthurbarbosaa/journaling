from django.db import models
from django.contrib.auth.models import User
class Journal(models.Model):
    highlight_text = models.CharField(max_length=255)
    is_habit_1_practiced = models.BooleanField(default=False)
    is_habit_2_practiced = models.BooleanField(default=False)
    tracking_value = models.FloatField()
class Goal(models.Model):
    name = models.CharField(max_length=255)
    is_done = models.BooleanField()
    