#!/usr/bin/python3
"""
This file is for declaring
and defining our User class.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    This class represents the User entity.

    The Attributes we'll be using:
        email (str): The email address of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    Return:
        None
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
