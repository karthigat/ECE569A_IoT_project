from django.db import models
from django.shortcuts import render
import os
from django.conf import settings
import requests
import json
# from homepage.get_location import FindCity
# Create your models here.

def upload_path(instance, filename):

    my_ip = requests.get('https://api.ipify.org').text
    # print(my_ip)
    geolocation_api = "your abstract api geolocation api key"
    # my_ip = "192.168.1.67"
    request_url = 'https://ipgeolocation.abstractapi.com/v1/?api_key=' + geolocation_api + '&ip_address=' + my_ip
    response = requests.get(request_url)
    result = response.content.decode()
    result = json.loads(result)
    city = result['city']
    # os.environ['Flag'] = "True"
    return '/'.join([city, filename])

class UploadFile(models.Model):
    file = models.FileField(upload_to=upload_path)

