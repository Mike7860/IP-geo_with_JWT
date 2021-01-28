from django.db import models


class LocationDatasByIp(models.Model):
    ip = models.CharField(max_length=200, primary_key=True, unique=True)
    country_name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)

    def __str__(self):
        return self.ip
