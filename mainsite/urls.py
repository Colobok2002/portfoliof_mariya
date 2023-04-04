from django.urls import re_path,path
from . import views

urlpatterns = [
    path('', views.index),
    path('nevs',views.nevs),
    path('<slug:slug>', views.aboyt_keus),
]