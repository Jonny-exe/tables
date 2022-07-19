from django.db import models

# Create your models here.
class Table(models.Model):
    lng = models.FloatField()
    lat = models.FloatField()
    image = models.CharField(max_length=300)