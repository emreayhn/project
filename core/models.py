from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.name}"