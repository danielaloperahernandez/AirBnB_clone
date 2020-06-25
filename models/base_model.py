#!/usr/bin/python3
"""Module for Base class"""
from datetime import datetime
import models
import uuid


class BaseModel:
    """Base class that defines all attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """Constructor method"""
        if kwargs != {} and kwargs is not None:
            
            
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
    def __str__(self):
        """string representation"""
        return "[" + type(self).__name__+"]" + "(" + self.id + ")" + \
                str(self.__dict__)
    
    def save(self):
        """updates the public instance attribute updated_at with the current
        datetime"""
        self.updated_at = datetime.now()
        
    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the
        instance"""
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        new_dict["__class__"] = type(self).__name__        
        return new_dict