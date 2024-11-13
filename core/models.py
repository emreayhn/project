from django.db import models
from django.utils import timezone

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(null=True)
    count_quiz = models.IntegerField(null=True)
    event_datetime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name}"