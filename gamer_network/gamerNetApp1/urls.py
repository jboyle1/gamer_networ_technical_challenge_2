from django.conf.urls import path
from gamerNetApp1 import views

urlpatterns = [
    path('', views.index, name='index')
]