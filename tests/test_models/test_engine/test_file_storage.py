#!/usr/bin/python3
"""
Module for FilStorage unittest
"""
import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review

class TestFileStorage(unittest.TestCase):
    """
    Unittests for testing FileStorage class.
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
        # Reset FileStorage instance
        FileStorage._FileStorage__entities = {}

    def test_instantiation(self):
        """Test instantiation of FileStorage."""
        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)

    def test_file_path_attribute(self):
        """Test file_path attribute."""
        storage = FileStorage()
        self.assertEqual(storage._FileStorage__file_path, "file.json")

    def test_entities_attribute(self):
        """Test entities attribute."""
        storage = FileStorage()
        self.assertEqual(storage._FileStorage__entities, {})

    def test_all(self):
        """Test all() method."""
        storage = FileStorage()
        all_objects = storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertEqual(all_objects, {})

    def test_new(self):
        """Test new() method."""
        storage = FileStorage()
        base_model = BaseModel()
        storage.new(base_model)
        self.assertIn("BaseModel." + base_model.id, storage.all())
        self.assertEqual(storage.all()["BaseModel." + base_model.id], base_model)

    def test_save(self):
        """Test save() method."""
        storage = FileStorage()
        base_model = BaseModel()
        storage.new(base_model)
        storage.save()
        with open("file.json", "r") as f:
            data = f.read()
            self.assertIn("BaseModel." + base_model.id, data)

    def test_reload(self):
        """Test reload() method."""
        storage = FileStorage()
        base_model = BaseModel()
        storage.new(base_model)
        storage.save()
        storage.reload()
        self.assertIn("BaseModel." + base_model.id, storage.all())

    def test_reload_empty_file(self):
        """Test reload() with empty file.json."""
        storage = FileStorage()
        storage.reload()
        self.assertEqual(storage.all(), {})

    def test_save_multiple_objects(self):
        """Test save() with multiple objects."""
        storage = FileStorage()
        base_model1 = BaseModel()
        base_model2 = BaseModel()
        storage.new(base_model1)
        storage.new(base_model2)
        storage.save()
        with open("file.json", "r") as f:
            data = f.read()
            self.assertIn("BaseModel." + base_model1.id, data)
            self.assertIn("BaseModel." + base_model2.id, data)

    def test_reload_multiple_objects(self):
        """Test reload() with multiple objects."""
        storage = FileStorage()
        base_model1 = BaseModel()
        base_model2 = BaseModel()
        storage.new(base_model1)
        storage.new(base_model2)
        storage.save()
        storage.reload()
        self.assertIn("BaseModel." + base_model1.id, storage.all())
        self.assertIn("BaseModel." + base_model2.id, storage.all())

    def test_save_and_reload_different_objects(self):
        """Test saving and reloading different object types."""
        storage = FileStorage()
        base_model = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        amenity = Amenity()
        review = Review()
        storage.new(base_model)
        storage.new(user)
        storage.new(state)
        storage.new(place)
        storage.new(city)
        storage.new(amenity)
        storage.new(review)
        storage.save()
        storage.reload()
        self.assertIn("BaseModel." + base_model.id, storage.all())
        self.assertIn("User." + user.id, storage.all())
        self.assertIn("State." + state.id, storage.all())
        self.assertIn("Place." + place.id, storage.all())
        self.assertIn("City." + city.id, storage.all())
        self.assertIn("Amenity." + amenity.id, storage.all())
        self.assertIn("Review." + review.id, storage.all())

if __name__ == '__main__':
    unittest.main()
