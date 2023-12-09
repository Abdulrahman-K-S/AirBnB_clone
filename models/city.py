#!/usr/bin/python3
"""City Module

This Module inherits from BaseModel class.
City Module contains the attributes to be assigned
to the cities.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """class City

    This is the class City

    Attributes:
        state_id (str): The UUID of the state the city belongs to.
        name (str): The city name.
    """
    state_id = ''
    name = ''
