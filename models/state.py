#!/usr/bin/python3
"""
This file is for declaring
and defining our State class.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    This class represents our State entity.

    Attributes:
        name (str): The name of the state.
    """
    name = ""
