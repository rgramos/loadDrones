from load_drones.celery import app


@app.task()
def drone_battery_level_history():
    from drones.models import Drone, BatteryHistoryLevel

    for drone in Drone.objects.all():
        BatteryHistoryLevel.objects.create(
            drone=drone,
            battery_capacity=drone.battery_capacity
        )
