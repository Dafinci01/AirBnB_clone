#!/usr/bin/python3
"""
Module for User class unittest
"""
import os
import unittest
from datetime import datetime
from time import sleep
from models.user import User
from models.base_model import BaseModel

class TestUser(unittest.TestCase):
    """
    Unittests for testing User class.
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
        """Test instantiation of User."""
        user = User()
        self.assertIsInstance(user, User)
        self.assertIsInstance(user, BaseModel)

    def test_attributes(self):
        """Test attributes of User."""
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertEqual(user.email, "")
        self.assertTrue(hasattr(user, "password"))
        self.assertEqual(user.password, "")
        self.assertTrue(hasattr(user, "first_name"))
        self.assertEqual(user.first_name, "")
        self.assertTrue(hasattr(user, "last_name"))
        self.assertEqual(user.last_name, "")

    def test_id_is_unique(self):
        """Test that each User instance has a unique ID."""
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_created_at_and_updated_at(self):
        """Test created_at and updated_at attributes."""
        user = User()
        self.assertIsInstance(user.created_at, datetime)
        self.assertIsInstance(user.updated_at, datetime)

    def test_str_representation(self):
        """Test string representation of User."""
        user = User()
        user.id = "12345"
        user.first_name = "John"
        user.last_name = "Doe"
        expected_str = f"[User] ({user.id}) {user.__dict__}"
        self.assertEqual(str(user), expected_str)

    def test_save(self):
        """Test save() method."""
        user = User()
        sleep(0.05)
        first_updated_at = user.updated_at
        user.save()
        self.assertLess(first_updated_at, user.updated_at)

    def test_to_dict(self):
        """Test to_dict() method."""
        user = User()
        user.email = "john.doe@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"
        user_dict = user.to_dict()
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['email'], 'john.doe@example.com')
        self.assertEqual(user_dict['password'], 'password123')
        self.assertEqual(user_dict['first_name'], 'John')
        self.assertEqual(user_dict['last_name'], 'Doe')
        self.assertIsInstance(user_dict['created_at'], str)
        self.assertIsInstance(user_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()
