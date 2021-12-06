from django.urls import path
from . import views
from django.conf.urls import include, url
# from .views import AWSUploadView


urlpatterns = [
   #path('', views.page, name='Mainpage'),
   path('',views.upload,name="index"),
   # path('',views.upload_city,name="index"),

  ]

