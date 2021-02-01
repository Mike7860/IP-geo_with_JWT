from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import LocationDatasByIp

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from .serializers import IpGeoSerializer
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from django.conf import settings
import requests


class DisplayDatas(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    #authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    # parser_classes = [JSONParser]

    serializer_class = IpGeoSerializer
    queryset = LocationDatasByIp.objects.all()

    #@csrf_exempt
    def get(self, request):
        return self.list(request)

    #@csrf_exempt
    def post(self, request):
        return self.create(request=request)


class DatasDetail(APIView):
    #@csrf_exempt
    def get_object(self, ip):
        try:
            return LocationDatasByIp.objects.get(ip=ip)
        except LocationDatasByIp.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    #@csrf_exempt
    def get(self, request, ip):
        item = self.get_object(ip)
        serializer = IpGeoSerializer(item)
        #if serializer.is_valid():
        return Response(serializer.data)

    #@csrf_exempt
    def delete(self, request, ip):
        item = self.get_object(ip)
        item.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
