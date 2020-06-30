#!/usr/bin/python3
"""Module for Base class"""
from datetime import datetime
import models
import uuid


class BaseModel:
    """Base class that defines all attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """Constructor method"""
        format_date = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for key, val kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(val, format_date)
                else:
                    self.__dict__[key] = val
        else:
            models.storage.new(self)

    def __str__(self):
        """string representation"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at with the current
        datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the
        instance"""
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        new_dict["__class__"] = type(self).__name__
        return new_dict
