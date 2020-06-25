#!/usr/bin/python3
"""Module for FileStorage class"""
import models
import json
import os

class FileStorage:
    """Class for serialization and deserialization to json format"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns __objects dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            dic_obj = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(dic_obj, file)

    def reload(self):
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
            obj_dict = json.load(file)
            obj_dict = {key: eval(value["__class__"])(**value) for key, value in obj_dict.items()}
            self.__objects = obj_dict
            """for k, value in (json.load(file)).items():
                value_get = eval(value["__class__"])(**value)
            self.__objects[k] = value"""