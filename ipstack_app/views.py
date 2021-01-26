from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import LocationDatasByIp

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS
from .serializers import IpGeoSerializer
from rest_framework import status
import requests

#hardcoded datas
key = "766ff3035ba594d83ad175ca7876a1aa"
ip = "109.206.193.138"
url = "http://api.ipstack.com/" + ip + "?access_key=" + key
response = requests.get(url).json()
print(response)

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class HelloView(APIView):
   # permission_classes = (IsAuthenticated, ReadOnly)
    key = "766ff3035ba594d83ad175ca7876a1aa"
    ip = "109.206.193.138"
    url = "http://api.ipstack.com/" + ip + "?access_key=" + key
    response = requests.get(url).json()

    def get(self, request):
        #content = {'message': 'Hello, World!'}
        key = "766ff3035ba594d83ad175ca7876a1aa"
        ip = "109.206.193.138"
        url = "http://api.ipstack.com/" + ip + "?access_key=" + key
        response = requests.get(url).json()
        return Response(response['ip'])


# ip = models.CharField(max_length=200)
# country_name = models.CharField(max_length=200)
# city = models.CharField(max_length=200)
# latitude = models.CharField(max_length=200)
# longidute = models.CharField(max_length=200)
# capital = models.CharField(max_length=200)


class DisplayDatas(APIView):
    @csrf_exempt
    def get(self, request):
        #if request.method == "GET":
        items = LocationDatasByIp.objects.all()
        serializer = IpGeoSerializer(items, many=True)
        #if serializer.is_valid():
        return Response(serializer.data)

#class AddDatas(APIView):
    @csrf_exempt
    def post(self, request):
        serializer = IpGeoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DatasDetail(APIView):
    @csrf_exempt
    def get_object(self, ip):
        try:
            return LocationDatasByIp.objects.get(ip=ip)
        except LocationDatasByIp.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    @csrf_exempt
    def get(self, request, ip):
        #if request.method == "GET":
        item = self.get_object(ip)
        serializer = IpGeoSerializer(item)
        #if serializer.is_valid():
        return Response(serializer.data)

    @csrf_exempt
    def delete(self, request, ip):
        item = self.get_object(ip)
        item.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

#
# class RemoveDatas(APIView):
#     @csrf_exempt
#     def delete(self, request, id):
#         item = self.get_object(id)
#         item.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)

