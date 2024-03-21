from django.db import models
from django.contrib.auth.models import User

class Journal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    highlight_text = models.TextField()

    habit_name = models.CharField(max_length=255)
    is_habit_practiced = models.BooleanField(default=False)

    tracking_name = models.CharField(max_length=255)
    tracking_value = models.FloatField()

    goal_name = models.CharField(max_length=255)
    is_goal_done = models.BooleanField()
