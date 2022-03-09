# load_drones

1. Install Requirements
 - Locate into directory loadDrones
 - run command "pip install -r requirements.txt"

2. Migrate
- Locate into directory loadDrones/loadDrones
- Run command "python manage.py migrate"

3. Load Required Data
- Locate into directory loadDrones/loadDrones
- Run command "python manage.py load_required_data"

4. Periodic Tasks Using Celery
- Pre requirements:
    * Install Redis
  
- Locate into directory loadDrones/loadDrones
- in terminal 1 run command "celery -A load_drones worker -P solo --loglevel=info"
- in terminal 2 run command "celery -A load_drones beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler"

5. Test
- Located in directory loadDrones/postman_collection_api_examples are a postman collection file. This collection can be loaded in to postman app or web to do api tests. In this collection are one api example for each endpoint. 