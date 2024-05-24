#!/usr/bin/python3
"""
Module for the User class, representing users of the system.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Represents user information.

    attributes:
        email (str): The email
        password (str): The pass
        first_name (str): The first name
        last_name (str): The last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
