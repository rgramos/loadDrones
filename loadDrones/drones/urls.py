from django.urls import path

from drones.views import RegisterDroneViewSet, CheckLoadedMedicationsItem, CheckAvailableDrones
from loadDrones.urls import routers

app_name = 'drones'

routers.register(r'register', RegisterDroneViewSet, basename='register')
routers.register(r'check-loaded-drone', CheckLoadedMedicationsItem, basename='check_loaded_drone')
routers.register(r'check-available-drones', CheckAvailableDrones, basename='check_available_drones')
urlpatterns = [] + routers.urls
