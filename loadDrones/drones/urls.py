from django.urls import path

from drones.views import RegisterDroneViewSet
from loadDrones.urls import routers

app_name = 'drones'

routers.register(r'register', RegisterDroneViewSet, basename='save_invoice')
urlpatterns = [] + routers.urls
