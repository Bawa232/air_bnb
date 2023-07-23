#!/usr/bin/python3
''' class that defines the attributes
and methods to be inherited by other classes
'''
from models import storage
from uuid import uuid4
from datetime import datetime


class BaseModel:


    def __init__(self, *args, **kwargs):
        ''' constructor method '''
        time_f = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            del kwargs["__class__"]
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, time_f)
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        clsName = self.__class__.__name__
        return f"{[clsName]} {(self.id)} {self.__dict__}"

    def save(self):
        '''updated everytime an instance is modified'''
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        ''' returns a dictionary representation of an instance '''
        todic = self.__dict__
        todic["__class__"] = self.__class__.__name__
        for key, value in todic.items():
            if isinstance(value, datetime):
                todic[key] = value.isoformat()
            else:
                todic[key] = value

        return todic
