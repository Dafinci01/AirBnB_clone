#!/usr/bin/python3
"""
Module for BaseModel unittest
"""
import os
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """
    Unittest for BaseModel
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

    def test_init(self):
        """Test instantiation of BaseModel."""
        model_instance = BaseModel()
        self.assertIsNotNone(model_instance.id)
        self.assertIsInstance(model_instance.id, str)
        self.assertIsNotNone(model_instance.created_at)
        self.assertIsInstance(model_instance.created_at, datetime)
        self.assertIsNotNone(model_instance.updated_at)
        self.assertIsInstance(model_instance.updated_at, datetime)

    def test_save(self):
        """Test save() method."""
        model_instance = BaseModel()
        sleep(0.05)
        first_updated_at = model_instance.updated_at
        model_instance.save()
        self.assertLess(first_updated_at, model_instance.updated_at)

    def test_to_dict(self):
        """Test to_dict() method."""
        model_instance = BaseModel()
        model_instance.name = "Test Model"
        model_dict = model_instance.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['name'], 'Test Model')
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_str_representation(self):
        """Test string representation of BaseModel."""
        model_instance = BaseModel()
        model_instance.id = "12345"
        model_instance.name = "Test Model"
        expected_str = f"[BaseModel] ({model_instance.id}) {model_instance.__dict__}"
        self.assertEqual(str(model_instance), expected_str)

if __name__ == '__main__':
    unittest.main()
