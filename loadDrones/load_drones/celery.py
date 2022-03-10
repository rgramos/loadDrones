from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'load_drones.settings')
app = Celery('load_drones')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    'checking-drone-battery-level': {
        'task': 'drones.tasks.drone_battery_level_history',
        'schedule': crontab(minute='*/30'),
        'args': (),
    },
}