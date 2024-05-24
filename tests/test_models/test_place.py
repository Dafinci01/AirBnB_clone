#!/usr/bin/python3
"""
Module for Place class unittest
"""
import os
import unittest
from datetime import datetime
from time import sleep
from models.place import Place
from models.base_model import BaseModel

class TestPlace(unittest.TestCase):
    """
    Unittests for testing Place class.
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
        """Test instantiation of Place."""
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertIsInstance(place, BaseModel)

    def test_attributes(self):
        """Test attributes of Place."""
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        self.assertEqual(place.city_id, "")
        self.assertTrue(hasattr(place, "user_id"))
        self.assertEqual(place.user_id, "")
        self.assertTrue(hasattr(place, "name"))
        self.assertEqual(place.name, "")
        self.assertTrue(hasattr(place, "description"))
        self.assertEqual(place.description, "")
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertEqual(place.number_rooms, 0)
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertEqual(place.number_bathrooms, 0)
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertEqual(place.max_guest, 0)
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertEqual(place.price_by_night, 0)
        self.assertTrue(hasattr(place, "latitude"))
        self.assertEqual(place.latitude, 0.0)
        self.assertTrue(hasattr(place, "longitude"))
        self.assertEqual(place.longitude, 0.0)
        self.assertTrue(hasattr(place, "amenity_ids"))
        self.assertEqual(place.amenity_ids, [])

    def test_id_is_unique(self):
        """Test that each Place instance has a unique ID."""
        place1 = Place()
        place2 = Place()
        self.assertNotEqual(place1.id, place2.id)

    def test_created_at_and_updated_at(self):
        """Test created_at and updated_at attributes."""
        place = Place()
        self.assertIsInstance(place.created_at, datetime)
        self.assertIsInstance(place.updated_at, datetime)

    def test_str_representation(self):
        """Test string representation of Place."""
        place = Place()
        place.id = "12345"
        place.name = "Test Place"
        expected_str = f"[Place] ({place.id}) {place.__dict__}"
        self.assertEqual(str(place), expected_str)

    def test_save(self):
        """Test save() method."""
        place = Place()
        sleep(0.05)
        first_updated_at = place.updated_at
        place.save()
        self.assertLess(first_updated_at, place.updated_at)

    def test_to_dict(self):
        """Test to_dict() method."""
        place = Place()
        place.name = "Test Place"
        place.city_id = "12345"
        place.user_id = "67890"
        place.description = "This is a test place."
        place.number_rooms = 2
        place.number_bathrooms = 1
        place.max_guest = 4
        place.price_by_night = 100
        place.latitude = 40.7128
        place.longitude = -74.0060
        place.amenity_ids = ["1", "2", "3"]
        place_dict = place.to_dict()
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertEqual(place_dict['name'], 'Test Place')
        self.assertEqual(place_dict['city_id'], '12345')
        self.assertEqual(place_dict['user_id'], '67890')
        self.assertEqual(place_dict['description'], 'This is a test place.')
        self.assertEqual(place_dict['number_rooms'], 2)
        self.assertEqual(place_dict['number_bathrooms'], 1)
        self.assertEqual(place_dict['max_guest'], 4)
        self.assertEqual(place_dict['price_by_night'], 100)
        self.assertEqual(place_dict['latitude'], 40.7128)
        self.assertEqual(place_dict['longitude'], -74.0060)
        self.assertEqual(place_dict['amenity_ids'], ["1", "2", "3"])
        self.assertIsInstance(place_dict['created_at'], str)
        self.assertIsInstance(place_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()
