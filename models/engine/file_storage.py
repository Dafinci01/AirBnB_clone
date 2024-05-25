#!/usr/bin/python3
'''
file storage module
'''

import json
from os import path

class FileStorage:
    '''
    serializes instances to a JSON file and deseri    alizes JSON file to instances
    Attributes:
        __filepath(str): path to the json file
        where the content will be stored
        __objects(dict): This will store all instance
        data
    '''
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''
        returns the dictionary __object
        '''
        return self.__objects

    def new(self, obj):
        '''
        adds an object to the __object dictionary
        attribute:
            obj: This is the object that you want
            to add to the  '__objects' dictionary
        '''
        class_name = obj.__class__.__name__
        object_id = obj.id
        key = class_name + '.' + object_id
        self.__objects[key] = obj

    def save(self):
        '''
        seralizes the dictionary to a json file
        '''
        json_dict = {}
        for k, v in self.__objects.items():
            json_dict[k] = v.to_dict()
        with open(self.__objects, mode='w', encoding='utf-8') as f:
            json.dump(json_dict, f)

    def reload(self):
        '''
        deserializes the JSON file to __objects
        '''
        if path.exists(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                json_dict = json.load(f)
            for k, v in json_dict.items():
                obj = self.class_dict[value['__class__']](**value)
                self.__objects[key] = obj
        

