from django.conf.urls import url
from django.urls import path

from . import views 

app_name = 'account'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('inscription/', views.inscription, name='inscription'),
  
   
]