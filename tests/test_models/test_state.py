#!/usr/bin/python3
""" This py file will make all the unit tests
for our class State and its objects"""

import unittest
from models.state import State
from datetime import datetime


class MyStateTest(unittest.TestCase):
    """Class for testing State"""

    def setUp(self):
        """Set up method"""
        self.state = State()

    def tearDown(self):
        """Tear down method"""
        del self.state

    def test_instance(self):
        """Test existence of attributes"""
        self.assertTrue(hasattr(self.state, "id"))
        self.assertTrue(hasattr(self.state, "created_at"))
        self.assertTrue(hasattr(self.state, "updated_at"))
        self.assertTrue(hasattr(self.state, "name"))

    def test_types(self):
        """Test types of attributes"""
        self.assertIsInstance(self.state.id, str)
        self.assertIsInstance(self.state.created_at, datetime)
        self.assertIsInstance(self.state.updated_at, datetime)
        self.assertIsInstance(self.state.name, str)


if __name__ == '__main__':
    unittest.main()
