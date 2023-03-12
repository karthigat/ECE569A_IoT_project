# Location of the computer
import requests
from requests import get
import json
import os
import shutil


my_ip = requests.get('https://api.ipify.org').text
print(my_ip)


def get_ip_location(my_ip):

    geolocation_api = "0e89983e41344f97a25ae1804602f0ac"
    ip_address = "206.116.135.77"
    request_url = 'https://ipgeolocation.abstractapi.com/v1/?api_key=' + geolocation_api + '&ip_address=' + ip_address
    response = requests.get(request_url)
    result = response.content.decode()
    result = json.loads(result)
    city = result['city']
    return city

City = get_ip_location(my_ip)
print(City)

home = os.path.expanduser('~')
location = os.path.join(home, 'Documents')
folder_check = os.path.isdir(location)
path = os.path.join(location, City)
print(path)
os.mkdir(path)
