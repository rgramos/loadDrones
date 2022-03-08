from django.urls import path

from drones.views import RegisterDroneViewSet, CheckLoadedMedicationsItem
from loadDrones.urls import routers

app_name = 'drones'

routers.register(r'register', RegisterDroneViewSet, basename='register')
routers.register(r'check-loaded-drone', CheckLoadedMedicationsItem, basename='check_loaded_drone')
urlpatterns = [] + routers.urls
