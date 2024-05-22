#!/usr/bin/python3
""" This py file will make all the unit tests
for our class User and its objects"""


import unittest
from models.user import User
from datetime import datetime


class MyUserTest(unittest.TestCase):
    """Class for testing User"""

    def setUp(self):
        """Set up method"""
        self.user = User()

    def tearDown(self):
        """Tear down method"""
        del self.user

    def test_instance(self):
        """Test existence and types of attributes"""
        attributes = ["id", "created_at", "updated_at", "email",
                      "password", "first_name", "last_name"]
        for attr in attributes:
            self.assertTrue(hasattr(self.user, attr))
            self.assertIsInstance(getattr(self.user, attr),
                                  str if attr == "id" else datetime if attr.endswith("_at") else str)


if __name__ == '__main__':
    unittest.main()
