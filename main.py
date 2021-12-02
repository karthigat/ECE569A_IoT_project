# Location of the computer
# from geolite2 import geolite2
# import socket
import requests
# from geopy.geocoders import Nominatim
from requests import get
import json
import os
import shutil
# from ip2geotools.databases.noncommercial import DbIpCity

my_ip = requests.get('https://api.ipify.org').text
print(my_ip)
# //folder
# path = os.path.join(os.environ["HOMEPATH"], "Document")
# print(path)
# shutil.copy(txtName, os.path.join(os.environ["HOMEPATH"], "Desktop"))

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
# print(home)
location = os.path.join(home, 'Documents')
# print(location)
folder_check = os.path.isdir(location)
# print(folder_check)
path = os.path.join(location, City)
print(path)
os.mkdir(path)
# save_path = 'C:/example/'
# name_of_file = input("What is the name of the file: ")
# completeName = os.path.join(save_path, name_of_file+".txt")
# file1 = open(completeName, "w")
# toFile = input("Write what you want into the field")
# file1.write(toFile)
# file1.close()
