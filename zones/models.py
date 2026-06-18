from django.db import models

class Zone(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    city = models.CharField(max_length=100)
    population = models.IntegerField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name