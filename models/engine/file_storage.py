#!/usr/bin/python3
"""Module for FileStorage class"""
from models.base_model import BaseModel
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
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            dic_obj = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(dic_obj, file)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists otherwise, do nothing"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
            obj_dict = json.load(file)
            obj_dict = {key: eval(value["__class__"])(**value) for key,
                        value in obj_dict.items()}
            self.__objects = obj_dict

    def find_classes(self):
        classes = {"BaseModel" : BaseModel}
        return classes