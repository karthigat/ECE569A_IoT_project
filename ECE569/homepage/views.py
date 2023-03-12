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
      geolocation_api = "0e89983e41344f97a25ae1804602f0ac"
      request_url = 'https://ipgeolocation.abstractapi.com/v1/?api_key=' + geolocation_api + '&ip_address=' + my_ip
      response = requests.get(request_url)
      print(type(response))
      result = response.content.decode()
      result = json.loads(result)
      city = result['city']
      if city is not None:
         return city
      else:
         return 'True'
  
def upload(request):
   context={}
   if request.method == 'POST':
      uploaded_file = request.FILES['upload']
      # manual location
      if request.POST.get("get") == 'submit to local' or request.POST.get("get") == 'submit to cloud':
         city = request.POST.get("city")
         if request.POST.get("get") == 'submit to local':
            path = os.path.expanduser("~")
            local_dir = os.path.join(path,"Documents")
            folder_check = os.path.isdir(local_dir)
            path = os.path.join(local_dir, city)
            fs = FileSystemStorage(location=path)
            name = fs.save(uploaded_file.name, uploaded_file)        
            messages.success(request, 'File saved successfully in Documents')
         if request.POST.get("get") == 'submit to cloud':
            upload = UploadFile.objects.create(file=uploaded_file)        
            messages.success(request, 'File saved successfully in S3 bucket')
      else:    
         # geolocation
         uploaded_file = request.FILES['upload']
         value = request.POST.get("msg")
         if value == "local":
            city_obj = FindCity()
            city = city_obj.get_ip_location()
            print(city)
            context={'city':city}
            if city is not 'True':

               path = os.path.expanduser("~")
               local_dir = os.path.join(path,"Documents")
               folder_check = os.path.isdir(local_dir)
               path = os.path.join(local_dir, city)
               fs = FileSystemStorage(location=path)
               name = fs.save(uploaded_file.name, uploaded_file)        
               messages.success(request, 'File saved successfully in Documents')
            else:
               messages.warning(request, 'City name not found and subit again')

         if value == "cloud":
            upload = UploadFile.objects.create(file=uploaded_file)        
            messages.success(request, 'File saved successfully in S3 bucket')
            
   return render(request, 'upload.html', context)
