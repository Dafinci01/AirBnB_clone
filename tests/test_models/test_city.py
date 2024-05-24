#!/usr/bin/python3
"""
Module for City unittest
"""
import os
import unittest
from datetime import datetime
from time import sleep
from models.city import City
from models.base_model import BaseModel

class TestCity(unittest.TestCase):
    """
    Unittests for testing City class.
    """

    def setUp(self):
        """Setup method for tests."""
        # Clear any existing file.json
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        """Teardown method for tests."""
        # Clear any existing file.json
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instantiation(self):
        """Test instantiation of City."""
        city = City()
        self.assertIsInstance(city, City)
        self.assertIsInstance(city, BaseModel)

    def test_attributes(self):
        """Test attributes of City."""
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertEqual(city.state_id, "")
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.name, "")

    def test_id_is_unique(self):
        """Test that each City instance has a unique ID."""
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)

    def test_created_at_and_updated_at(self):
        """Test created_at and updated_at attributes."""
        city = City()
        self.assertIsInstance(city.created_at, datetime)
        self.assertIsInstance(city.updated_at, datetime)

    def test_str_representation(self):
        """Test string representation of City."""
        city = City()
        city.id = "12345"
        city.name = "Test City"
        expected_str = f"[City] ({city.id}) {city.__dict__}"
        self.assertEqual(str(city), expected_str)

    def test_save(self):
        """Test save() method."""
        city = City()
        sleep(0.05)
        first_updated_at = city.updated_at
        city.save()
        self.assertLess(first_updated_at, city.updated_at)

    def test_to_dict(self):
        """Test to_dict() method."""
        city = City()
        city.name = "Test City"
        city.state_id = "12345"
        city_dict = city.to_dict()
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertEqual(city_dict['name'], 'Test City')
        self.assertEqual(city_dict['state_id'], '12345')
        self.assertIsInstance(city_dict['created_at'], str)
        self.assertIsInstance(city_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()
