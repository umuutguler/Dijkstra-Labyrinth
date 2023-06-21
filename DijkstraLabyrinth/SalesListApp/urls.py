
from django.urls import path

from SalesListApp.views import hepsiburadaApi
from rest_framework import routers
from . import views
"""
router = routers.DefaultRouter()
router.register(r'HepsiBurada/', views.hepsiburadaApi)

urlpatterns = [
    path('^$', hepsiburadaApi, name='hepsiburadaApi'),
    path('SalesListApp/', include('SalesListApp.urls'))
]

urlpatterns += router.urls
"""
urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home),
    path("home/<int:id>", views.pc_details, name="pc_details"),

]
