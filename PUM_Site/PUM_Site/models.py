from django.db import models

class News(models.Model):
    date = models.DateTimeField()
    header = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    link = models.CharField(max_length=255)