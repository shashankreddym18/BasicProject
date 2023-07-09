from django.db import models

class Frequency(models.Model):
    value = models.FloatField()

    def __str__(self):
        return str(self.value)
