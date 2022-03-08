from drones.views import RegisterDroneViewSet, CheckLoadedMedicationsItem, CheckAvailableDrones, CheckDroneBatteryLevel
from loadDrones.urls import routers

app_name = 'drones'

routers.register(r'register', RegisterDroneViewSet, basename='register')
routers.register(r'check-loaded-drone', CheckLoadedMedicationsItem, basename='check_loaded_drone')
routers.register(r'check-available-drones', CheckAvailableDrones, basename='check_available_drones')
routers.register(r'check-drone-battery', CheckDroneBatteryLevel, basename='check_drone_battery')
urlpatterns = [] + routers.urls
