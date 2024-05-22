#!/usr/bin/python3
""" This py file will make all the unit tests
for our class Place and its objects"""

import unittest
from models.place import Place
from datetime import datetime


class MyPlaceTest(unittest.TestCase):

    def test_attributes_existence(self):
        """Test the existence of our attributes"""
        new = Place()
        self.assertTrue(hasattr(new, "id"))
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))
        self.assertTrue(hasattr(new, "city_id"))
        self.assertTrue(hasattr(new, "user_id"))
        self.assertTrue(hasattr(new, "name"))
        self.assertTrue(hasattr(new, "description"))
        self.assertTrue(hasattr(new, "number_rooms"))
        self.assertTrue(hasattr(new, "number_bathrooms"))
        self.assertTrue(hasattr(new, "max_guest"))
        self.assertTrue(hasattr(new, "price_by_night"))
        self.assertTrue(hasattr(new, "latitude"))
        self.assertTrue(hasattr(new, "longitude"))
        self.assertTrue(hasattr(new, "amenity_ids"))

    def test_attribute_types(self):
        """Test the types of attributes"""
        new = Place()
        attribute_types = {
            "id": str,
            "created_at": datetime,
            "updated_at": datetime,
            "city_id": str,
            "user_id": str,
            "name": str,
            "description": str,
            "number_rooms": int,
            "number_bathrooms": int,
            "max_guest": int,
            "price_by_night": int,
            "latitude": float,
            "longitude": float,
            "amenity_ids": list
        }
        for attr, attr_type in attribute_types.items():
            with self.subTest(attr=attr):
                self.assertIsInstance(getattr(new, attr), attr_type)


if __name__ == '__main__':
    unittest.main()
