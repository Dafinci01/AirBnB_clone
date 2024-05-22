#!/usr/bin/python3
"""
MThis file is for declaring
and defining our Amenity class.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    This class represents our Amenity entity.

    The Attributes we'll be using:
        name (str): The name of the amenity.

    Return:
        None
    """
    name = ""
