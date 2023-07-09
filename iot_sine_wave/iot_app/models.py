# Create your models here.
from django.db import models

class SineWave(models.Model):
    frequency = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
