#!/usr/bin/python3
"""Unit test for Amenity"""

import unittest
from models.amenity import Amenity
from datetime import datetime


class MyAmenityTest(unittest.TestCase):
    """Class for testing our Amenity model"""

    def setUp(self):
        """Set up method"""
        self.amenity = Amenity()

    def tearDown(self):
        """Tear down method"""
        del self.amenity

    def test_instance(self):
        """Test existence of attributes"""
        self.assertTrue(hasattr(self.amenity, "id"))
        self.assertTrue(hasattr(self.amenity, "created_at"))
        self.assertTrue(hasattr(self.amenity, "updated_at"))
        self.assertTrue(hasattr(self.amenity, "name"))

    def test_types(self):
        """Test types of attributes"""
        self.assertIsInstance(self.amenity.id, str)
        self.assertIsInstance(self.amenity.created_at, datetime)
        self.assertIsInstance(self.amenity.updated_at, datetime)
        self.assertIsInstance(self.amenity.name, str)


if __name__ == '__main__':
    unittest.main()
