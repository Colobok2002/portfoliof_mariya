from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('admin/',views.admin_redirect),
    path('admin', admin.site.urls),
    path(r'', include(('mainsite.urls', 'site'))),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'mainsite.views.referect_to_nome'