from django.urls import re_path,path
from . import views

urlpatterns = [
    path('add_zap', views.add_zap),
    path('nevs',views.nevs),
    path('', views.index),
    path('<slug:slug>', views.aboyt_keus),

]