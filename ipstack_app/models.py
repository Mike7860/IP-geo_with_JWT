from django.db import models


class LocationDatasByIp(models.Model):
    ip = models.CharField(max_length=200, primary_key=True, unique=True)
    #type = models.CharField(max_length=200)
    #continent_code = models.CharField(max_length=200)
    #continent_name = models.CharField(max_length=200)
    #country_code = models.CharField(max_length=200)
    country_name = models.CharField(max_length=200)
    #region_code = models.CharField(max_length=200)
    #region_name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    #zip = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    #geoname_id = models.CharField(max_length=200)
    #capital = models.CharField(max_length=200)
    #code = models.CharField(max_length=200)
    #name = models.CharField(max_length=200)
    #native = models.CharField(max_length=200)
    #country_flag = models.CharField(max_length=200)
    #country_flag_emoji = models.CharField(max_length=200)
    #country_flag_emoji_unicode = models.CharField(max_length=200)
    #calling_code = models.IntegerField(max_length=200)
    #is_eu = models.BooleanField(max_length=200)

    def __str__(self):
        return self.ip
