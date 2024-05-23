#!/usr/bin/python3
"""
Module for the BaseModel class, providing a base model for other classes.
"""
import uuid
from datetime import datetime

import models


class BaseModel:
    """
    Base class for other classes.

    Attributes:
        id (str): The unique identifier for each instance.
        created_at (datetime): The creation timestamp of the instance.
        updated_at (datetime): The last update timestamp of the instance.
    """
    def __init__(self, *args, **kwargs):
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, time_format))
                else:
                    setattr(self, key, value)

        models.storage.new(self)

    def save(self):
        """
        Returns a dictionary representation of the instance attributes.
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def dictify(self):
        """
        Converts the instance attributes to a dictionary representation.

        Returns:
            dict: A dictionary containing the instance attributes.
        """
        dict_instance = self.__dict__.copy()
        dict_instance["__class__"] = self.__class__.__name__
        dict_instance["created_at"] = self.created_at.isoformat()
        dict_instance["updated_at"] = self.updated_at.isoformat()

        return dict_instance

    def __str__(self):

        """
        Returns a string representation of the instance.

        Returns:
            str: A string representation of the instance.
        """

        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)


if __name__ == "__main__":
    model_instance = BaseModel()
    model_instance.name = "My_First_Model"
    model_instance.my_number = 89
    print(model_instance.id)
    print(model_instance)
    print(type(model_instance.created_at))
    print("--")
    model_instance_json = model_instance.dictify()
    print(model_instance_json)
    print("JSON of model_instance:")
    for key in model_instance_json.keys():
        print("\t{}: ({}) - {}".format(key, type(model_instance_json[key]), model_instance_json[key]))

    print("--")
    new_model_instance = BaseModel(**model_instance_json)
    print(new_model_instance.id)
    print(new_model_instance)
    print(type(new_model_instance.created_at))

    print("--")
    print(model_instance is new_model_instance)
