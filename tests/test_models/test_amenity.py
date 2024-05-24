#!/usr/bin/python3
"""
Module for Amenity class unittest
"""
import os
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity
from models.base_model import BaseModel

class TestAmenity(unittest.TestCase):
    """
    Unittests for testing Amenity class.
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
        """Test instantiation of Amenity."""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity, BaseModel)

    def test_attributes(self):
        """Test attributes of Amenity."""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")

    def test_id_is_unique(self):
        """Test that each Amenity instance has a unique ID."""
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.id, amenity2.id)

    def test_created_at_and_updated_at(self):
        """Test created_at and updated_at attributes."""
        amenity = Amenity()
        self.assertIsInstance(amenity.created_at, datetime)
        self.assertIsInstance(amenity.updated_at, datetime)

    def test_str_representation(self):
        """Test string representation of Amenity."""
        amenity = Amenity()
        amenity.id = "12345"
        amenity.name = "Test Amenity"
        expected_str = f"[Amenity] ({amenity.id}) {amenity.__dict__}"
        self.assertEqual(str(amenity), expected_str)

    def test_save(self):
        """Test save() method."""
        amenity = Amenity()
        sleep(0.05)
        first_updated_at = amenity.updated_at
        amenity.save()
        self.assertLess(first_updated_at, amenity.updated_at)

    def test_to_dict(self):
        """Test to_dict() method."""
        amenity = Amenity()
        amenity.name = "Test Amenity"
        amenity_dict = amenity.to_dict()
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertEqual(amenity_dict['name'], 'Test Amenity')
        self.assertIsInstance(amenity_dict['created_at'], str)
        self.assertIsInstance(amenity_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()
