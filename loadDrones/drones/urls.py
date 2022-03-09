from drones.views import RegisterDroneViewSet, CheckLoadedMedicationsItemViewSet, CheckAvailableDronesViewSet, \
    CheckDroneBatteryLevelViewSet, LoadingDroneViewSet
from loadDrones.urls import routers

app_name = 'drones'

routers.register(r'register', RegisterDroneViewSet, basename='register')
routers.register(r'check-loaded-drone', CheckLoadedMedicationsItemViewSet, basename='check_loaded_drone')
routers.register(r'check-available-drones', CheckAvailableDronesViewSet, basename='check_available_drones')
routers.register(r'check-drone-battery', CheckDroneBatteryLevelViewSet, basename='check_drone_battery')
routers.register(r'load-medication-drone', LoadingDroneViewSet, basename='load_medication_drone')
urlpatterns = [] + routers.urls
