"""
    yazlab1 URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

from SalesListApp.views import hepsiburadaApi



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('SalesListApp.urls'))

    #path('', hepsiburadaApi, name='hepsiburadaApi'),
    #path('SalesListApp/', include('SalesListApp.urls')),
]
