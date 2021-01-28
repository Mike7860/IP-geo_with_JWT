from rest_framework import serializers
from django.conf import settings
from .models import LocationDatasByIp
import requests


class IpGeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationDatasByIp
        fields = ['ip', 'country_name', 'city', 'latitude', 'longitude']

    def create(self, validated_data):
        key = settings.IPSTACK_APP_KEY
        #ip = "109.206.193.131"
        ip = validated_data['ip']
        url = "http://api.ipstack.com/" + ip + "?access_key=" + key
        response = requests.get(url).json()
        country_name = response['country_name']
        city = response['city']
        latitude = response['latitude']
        longitude = response['longitude']
        print(response)
        #return Response(response['ip'])
        from_external_api = LocationDatasByIp.objects.create(ip=ip, country_name=country_name, city=city,
                                                             latitude=latitude, longitude=longitude)
        return from_external_api

    # def update(self, instance, validated_data):
    #     instance.ip = validated_data.get('ip', instance.ip)
    #     instance.country_name = validated_data.get('country_name', instance.country_name)
    #     #instance.region_name = validated_data.get('region_name', instance.region_name)
    #     instance.city = validated_data.get('city', instance.city)
    #     #instance.zip = validated_data.get('zip', instance.zip)
    #     instance.latitude = validated_data.get('latitude', instance.latitude)
    #     instance.longidute = validated_data.get('longidute', instance.longidute)
    #     instance.capital = validated_data.get('capital', instance.capital)
    #     instance.save()
    #     return instance


