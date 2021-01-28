from rest_framework import serializers
from django.conf import settings
from .models import LocationDatasByIp
import requests


class IpGeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationDatasByIp
        fields = ['ip', 'country_name', 'city', 'latitude', 'longitude']
        extra_kwargs = {'country_name': {'required': False}, 'city': {'required': False},
                        'latitude': {'required': False}, 'longitude': {'required': False,
         }}

    def create(self, validated_data):
        key = settings.IPSTACK_APP_KEY
        ip = validated_data['ip']
        url = "http://api.ipstack.com/" + ip + "?access_key=" + key
        response = requests.get(url).json()
        country_name = response['country_name']
        city = response['city']
        latitude = response['latitude']
        longitude = response['longitude']

        try:
            from_external_api = LocationDatasByIp.objects.create(ip=ip, country_name=country_name, city=city,
                                                             latitude=latitude, longitude=longitude)
        except:
            raise Exception("Wrong IP address")

        return from_external_api



