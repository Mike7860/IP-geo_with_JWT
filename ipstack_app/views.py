from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

import requests

# hardcoded datas
# key = "766ff3035ba594d83ad175ca7876a1aa"
# ip = "5.172.255.6"
# # url = "http://api.ipstack.com/" + ip + "?access_key=" + key
# # response = requests.get(url).json()
# # print(response['longitude'])
#
#
# def lng_lat_from_ip(ip, key):
#     url = "http://api.ipstack.com/" + ip + "?access_key=" + key
#     response = requests.get(url).json()
#     return (response['longitude'], response['latitude'])
#
#
# longitude, latitude = lng_lat_from_ip(ip, key)
#
# url = 'http://127.0.0.1:8000/hello/'
# headers = {'Authorization': 'Token 20fa04ccd3ea24f8c2e5b156e46b38ae39cafc510a'}
# r = requests.get(url, headers=headers)


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
