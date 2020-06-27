#!/usr/bin/python3
"""Module for FileStorage class"""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json
import os


class FileStorage:
    """Class for serialization and deserialization to json format"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns __objects dictionary"""
        return {key: value for key, value in self.__objects.items()}

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Save function """
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict.update({key: value.to_dict()})
        json_file = json.dumps(new_dict)
        with open(FileStorage.__file_path, "w") as file:
            file.write(json_file)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists otherwise, do nothing"""
        my_dict = {"BaseModel": BaseModel, "User": User, "State": State,
                   "City": City, "Amenity": Amenity, "Place": Place,
                   "Review": Review}
        json_file = ""
        try:
            with open(FileStorage.__file_path, "r") as file:
                json_file = json.loads(file.read())
                for key in json_file:
                    self.__objects[key] = my_dict[
                        json_file[key]['__class__']](**json_file[key])
        except:
            pass
        
    def delete(self, obj=None):
        """delete obj (called in to_destroy)"""
        if obj:
            try:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                del self.__objects[key]
                self.save()
            except:
                pass
