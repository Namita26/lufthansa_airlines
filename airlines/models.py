from django.db import models
from datetime import datetime


class LinksInformation(models.Model):
    link = models.URLField(blank=True)
    status = models.IntegerField(blank=True)
    time_of_verification = models.DateTimeField(default=datetime.now)
    level = models.IntegerField()
    url_hash = models.CharField(primary_key=True, max_length=250)
