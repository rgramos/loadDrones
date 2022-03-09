# load_drones

CELERY:

Terminal 1:

celery -A load_drones beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler


Terminal 2:

celery -A load_drones worker -P solo --loglevel=info