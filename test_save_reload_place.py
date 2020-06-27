#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.place import Place

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new User --")
my_place = Place()
my_place.city_id = "city_id"
my_place.user_id = "user_id"
my_place.name = "Betty"
my_place.description = "pretty"
my_place.number_rooms = 20
my_place.bathrooms = 21
my_place.max_guest = 120
my_place.price_by_night = 70000
my_place.latitude = 12.3
my_place.longitude = 45.78
my_place.amenity_ids = []
my_place.save()
print(my_place)

print("-- Create a new User 2 --")
my_place2 = Place()
my_place2.city_id = "city_id2"
my_place2.user_id = "user_id2"
my_place2.name = "Betty2"
my_place2.description = "pretty2"
my_place2.number_rooms = 23
my_place2.bathrooms = 24
my_place2.max_guest = 125
my_place2.price_by_night = 80000
my_place2.latitude = 12.67
my_place2.longitude = 45.00
my_place2.amenity_ids = []
my_place2.save()
print(my_place2)