#!/usr/bin/python3
""" Unit test for City """
import unittest
from models.city import City
from datetime import datetime


class CityTestCase(unittest.TestCase):
    """ Class for City test """

    def setUp(self):
        """ Set up a City instance for testing """
        self.city = City()

    def tearDown(self):
        """ Clean up after each test """
        del self.city

    def test_existence(self):
        """ Test existence of attributes """
        self.assertTrue(hasattr(self.city, "id"))
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertTrue(hasattr(self.city, "updated_at"))
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))

    def test_types(self):
        """ Test types of attributes """
        self.assertIsInstance(self.city.id, str)
        self.assertIsInstance(self.city.created_at, datetime)
        self.assertIsInstance(self.city.updated_at, datetime)
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)


if __name__ == '__main__':
    unittest.main()
