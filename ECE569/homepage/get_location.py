# Create your views here.
from django.shortcuts import render
import os
from django.conf import settings
import requests
import json
# from .models import Upload


class FindCity(object):

   def get_ip_location(self):
      my_ip = requests.get('https://api.ipify.org').text
      # print(my_ip)
      geolocation_api = "0e89983e41344f97a25ae1804602f0ac"
      # my_ip = "192.168.1.67"
      request_url = 'https://ipgeolocation.abstractapi.com/v1/?api_key=' + geolocation_api + '&ip_address=' + my_ip
      response = requests.get(request_url)
      result =response.content.decode()
      result = json.loads(result)
      city = result['city']
      if city is not None:
         return city
      else:
         return False
# 