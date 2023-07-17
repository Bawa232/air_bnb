#!/usr/bin/python3
''' class that defines the attributes
and methods to be inherited by other classes
'''


from uuid import uuid4
from datetime import datetime


class BaseModel:


    
    def __init__(self):
        ''' constructor method '''
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        clsName = self.__class__.__name__
        return f"{[clsName]} {(self.id)} {self.__dict__}"

    def save(self):
        '''updated everytime an instance is modified'''
        self.updated_at = datetime.now()

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
