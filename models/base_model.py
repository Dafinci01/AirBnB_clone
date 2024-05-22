#!/usr/bin/python3
"""
Module for the Base Class
"""

import models
import uuid
from datetime import datetime


class BaseModel:
    '''
    This is the base model that takes care of
    the initialization, serialization and dese
    rialization of your future instances

    Attributes:
        - id(str): This is an UUID for when an        instance is created
        - created_at(datetime): This will assi
        gn  instance with date & time it was
        created
        - updated_at(datetime): This will assi
        gn instance with date & time it was up
        dated
    '''

    def __init__(self, *args, **kwargs):
        '''
        initializes attributes: id, created_at,
        updated_at
        '''

        dateformat = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for key, value in kwargs.items():
                if "__class__" == key:
                    continue
                if "created_at" == key:
                    self.created_at = datetime.strptime(
                        kwargs["created_at"], dateformat)
                elif "updated_at" == key:
                    self.updated_at = datetime.strptime(
                        kwargs["updated_at"], dateformat)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        '''
        This function prints the content of the
        'BaseModel' class using the format

        $ [<class name>] (<self.id>)
        <self.__dict__>

        Example:
            $ my_m = BaseModel()
            $ my_m.name = "My First Model"
            $ my_m.num = 89
            $ print(my_m)
        '''

        return '[{}] ({}) {}'.format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        '''
        updates the public instance attribute
        'updated_at' with the current datetime
        & save to a file
        '''

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''
        returns a dictionary containing all keys/v
        alues of '__dict__' of the instance:
        '''

        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict
