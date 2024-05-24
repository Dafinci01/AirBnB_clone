#!/usr/bin/python3
"""
Module for State unittest
"""
import os
import unittest
from datetime import datetime
from time import sleep
from models.state import State
from models.base_model import BaseModel

class TestState(unittest.TestCase):
    """
    Unittests for testing State class.
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
        """Test instantiation of State."""
        state = State()
        self.assertIsInstance(state, State)
        self.assertIsInstance(state, BaseModel)

    def test_attributes(self):
        """Test attributes of State."""
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")

    def test_id_is_unique(self):
        """Test that each State instance has a unique ID."""
        state1 = State()
        state2 = State()
        self.assertNotEqual(state1.id, state2.id)

    def test_created_at_and_updated_at(self):
        """Test created_at and updated_at attributes."""
        state = State()
        self.assertIsInstance(state.created_at, datetime)
        self.assertIsInstance(state.updated_at, datetime)

    def test_str_representation(self):
        """Test string representation of State."""
        state = State()
        state.id = "12345"
        state.name = "Test State"
        expected_str = f"[State] ({state.id}) {state.__dict__}"
        self.assertEqual(str(state), expected_str)

    def test_save(self):
        """Test save() method."""
        state = State()
        sleep(0.05)
        first_updated_at = state.updated_at
        state.save()
        self.assertLess(first_updated_at, state.updated_at)

    def test_to_dict(self):
        """Test to_dict() method."""
        state = State()
        state.name = "Test State"
        state_dict = state.to_dict()
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertEqual(state_dict['name'], 'Test State')
        self.assertIsInstance(state_dict['created_at'], str)
        self.assertIsInstance(state_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()
