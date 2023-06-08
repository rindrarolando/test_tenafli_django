from django.db import models

class School(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    percent_african_american = models.FloatField()

    def __str__(self):
        return self.name
