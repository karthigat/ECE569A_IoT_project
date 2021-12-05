from django.shortcuts import render
from django.http import HttpResponse
import os
from django.conf import settings
from django.views.generic import TemplateView 
from django.core.files.storage import FileSystemStorage
import requests
import json
from .models import UploadFile
from django.contrib import messages

class FindCity(object):

   def get_ip_location(self):
      context = {}
      my_ip = requests.get('https://api.ipify.org').text
      # print(my_ip)
      geolocation_api = "your abstract api geolocation api key"
      # my_ip = "192.168.1.67"
      request_url = 'https://ipgeolocation.abstractapi.com/v1/?api_key=' + geolocation_api + '&ip_address=' + my_ip
      response = requests.get(request_url)
      result = response.content.decode()
      result = json.loads(result)
      city = result['city']
      if city is not None:
         return city
      else:
         #return False
         return render(requests, 'upload.html', context)
         # render('upload.html', {'status':True})

def upload(request):
   context = {}
   if request.method == 'POST':
      uploaded_file = request.FILES['upload']
      value = request.POST.get("msg")
      if value == "local":
         city_obj = FindCity()
         city = city_obj.get_ip_location()
         path = os.path.expanduser("~")
         local_dir = os.path.join(path,"Documents")
         folder_check = os.path.isdir(local_dir)
         path = os.path.join(local_dir, city)
         fs = FileSystemStorage(location=path)
         # fs = FileSystemStorage(location=local_dir)
         name = fs.save(uploaded_file.name, uploaded_file)        
         messages.success(request, 'File saved successfully in Documents')
      # context['url'] = fs.url(name)

      if value == "cloud":
         upload = UploadFile.objects.create(file=uploaded_file)        
         messages.success(request, 'File saved successfully in S3 bucket')
         
      # upload = UploadFile.objects.all()
      # fs = FileSystemStorage()
      # name = fs.save(uploaded_file.name, uploaded_file)
      # context['url'] = fs.url(name)
   return render(request, 'upload.html', context)
      # return render(request, 'upload.html')






