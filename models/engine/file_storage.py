#!/usr/bin/python3
"""
This module handles the serialization and deserialization of data to and from storage.
"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City


class FileStorage:
    """
    FileStorage class responsible for storing, serializing, and deserializing data to and from a file.
    """
    __file_path = "file.json"

    __entities = {}

    def new(self, entity):
        """
        Stores an objects in the __entities dictionary using a key formatted as <entity class name>.id.
        """

        entity_cls_name = entity.__class__.__name__

        key = "{}.{}".format(entity_cls_name, entity.id)

        FileStorage.__entities[key] = entity


    def all(self):
        """
        Returns the __entities dictionary, providing access to all stored entities.
        """
        return  FileStorage.__entities


    def save(self):
        """
        Serializes the __entities dictionary to JSON format and saves it to the file specified by __file_path.
        """
        all_entitys = FileStorage.__entities

        entity_dict = {}

        for entity in all_entitys.keys():
            entity_dict[entity] = all_entitys[entity].dictify()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(entity_dict, file)

    def reload(self):
        """
        Deserializes the JSON file specified by __file_path and loads the data into the __entities dictionary.
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    entity_dict = json.load(file)

                    for key, value in entity_dict.items():
                        class_name, entity_id = key.split('.')

                        cls = eval(class_name)

                        instance = cls(**value)

                        FileStorage.__entities[key] = instance
                except Exception:
                    pass
