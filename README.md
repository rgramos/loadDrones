# load_drones

Previous requirements
- $ git clone https://github.com/rgramos/loadDrones.git

#1. Install Requirements
 - Locate into directory loadDrones
 - Run command:
>pip install -r requirements.txt

#2. Migrate
- Locate into directory loadDrones/loadDrones
- Run command:
>python manage.py migrate

#3. Load Required Data
- Locate into directory loadDrones/loadDrones
- Run command:
> python manage.py load_required_data

#4. Periodic Tasks Using Celery
- Pre requirements:
    * Install Redis
  
- Locate into directory loadDrones/loadDrones
- in terminal 1 run command:
>celery -A load_drones worker -P solo --loglevel=info
- in terminal 2 run command:
>celery -A load_drones beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler

5. Test
- Located in directory loadDrones/postman_collection_api_examples are a postman collection file. This collection can be loaded in to postman app or web to do api tests. In this collection are one api example for each endpoint. 
- For unit tests run command:
> python manage.py test


#Run server
> python manage.py runserver

#Api Endpoints
Note: Var {{server_host}} is url from server. Ex. http://127.0.0.1:8000
- Register Drone
````
#URL
{{server_host}}/drones/register/

#Method Post

#Request Parameters

serial_number: String
weight_limiter: Float
battery_capacity: Integer
model: String (Options: Lightweight | Middleweight | Cruiserweight | Heavyweight)

#Response
Object: Drone

Example
{
    "id": "fa48d57a-f4c8-427f-97dd-4d6352b176fe",
    "created": "2022-03-09T21:23:28.623879Z",
    "updated": "2022-03-09T21:23:28.623879Z",
    "serial_number": "Test Drone",
    "weight_limiter": 300,
    "battery_capacity": 100,
    "model": "Heavyweight"
}
````

- Check Loaded Drone
````
#URL
{{server_host}}/drones/check-loaded-drone/<drone_id>/

#Method Get

#Request Parameters

None

#Response
Object: List[ Medications ] | message: string

Example 1
[
  {
      "id": "fa48d57a-f4c8-427f-97dd-4d6352b176fe",
      "name": "Test Drone",
      "weight": 300,
      "code": AS12,
      "image": ""
  }
]


Example 2

{
    "message": "Drone not loaded"
}


````

- Check Available Drones
````
#URL
{{server_host}}/drones/check-available-drones

#Method Get

#Request Parameters

None

#Response
Object: List[ Drones ] | List []

Example 1
[
    {
        "id": "6dc381f3-3037-4602-a25f-002a383fe921",
        "serial_number": "27736",
        "weight_limiter": 400,
        "battery_capacity": 77,
        "model": "Cruiserweight",
        "state": "IDLE"
    },
    {
        "id": "fa48d57a-f4c8-427f-97dd-4d6352b176fe",
        "serial_number": "Test Drone",
        "weight_limiter": 300,
        "battery_capacity": 100,
        "model": "Heavyweight",
        "state": "IDLE"
    }
]


Example 2

[]


````

- Check Drone Level Battery
````
#URL
{{server_host}}/drones/check-drone-battery/<drone_id>/

#Method Get

#Request Parameters

None

#Response
Object: "battery_capacity": Integer

Example 1
{
    "battery_capacity": 77
}

````

- Load Medication Drone
````
#URL
{{server_host}}/drones/load-medication-drone/

#Method Post

#Request Parameters

drone: <UUID:Drones>
medications: [ <UUID:Medications> ]

#Response
Object: "message": String

Example
{
    "message": "Successfully loaded drone"
}
````