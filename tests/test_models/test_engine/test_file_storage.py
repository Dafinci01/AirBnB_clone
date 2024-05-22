#!/usr/bin/python3
"""Unit tests for FileStorage class"""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models
import json
import os


class MyFileStorageTest(unittest.TestCase):

    def setUp(self):
        """Set up for each test"""
        self.storage = FileStorage()
        self.file_path = FileStorage.get_file_path()

        # Clean up the file before each test
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def tearDown(self):
        """Tear down after each test"""
        # Clean up the file after each test
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        self.storage.get_objects().clear()  # Clear objects dictionary

    def test_file_storage_init(self):
        """Test initialization and class attributes"""
        filepath = FileStorage.get_file_path()
        _objs = self.storage.get_objects()  # Access objects via instance
        self.assertEqual(filepath, "file.json")
        self.assertIsInstance(filepath, str)
        self.assertIsInstance(_objs, dict)

    def test_base_model_methods(self):
        """Test methods of BaseModel"""
        new = BaseModel()
        self.assertTrue(hasattr(new, "__init__"))
        self.assertTrue(hasattr(new, "__str__"))
        self.assertTrue(hasattr(new, "save"))
        self.assertTrue(hasattr(new, "to_dict"))

    def test_all(self):
        """Test all method"""
        new = BaseModel()
        self.storage.new(new)
        self.assertIsInstance(self.storage.all(), dict)
        self.assertNotEqual(self.storage.all(), {})

    def test_new(self):
        """Test new method"""
        new = BaseModel()
        self.storage.new(new)
        keyname = "BaseModel." + new.id
        self.assertIsInstance(self.storage.all()[keyname], BaseModel)
        self.assertEqual(self.storage.all()[keyname], new)
        self.assertIn(keyname, self.storage.all())
        self.assertTrue(self.storage.all()[keyname] is new)

    def test_save(self):
        """Test save method"""
        new = BaseModel()
        self.storage.new(new)
        self.storage.save()
        with open(self.file_path, 'r') as file:
            saved_data = json.load(file)
        keyname = "BaseModel." + new.id
        self.assertIn(keyname, saved_data)
        self.assertEqual(saved_data[keyname], new.to_dict())

    def test_reload(self):
        """Test reload method"""
        new = BaseModel()
        self.storage.new(new)
        self.storage.save()
        self.storage.all().clear()
        self.storage.reload()
        with open(self.file_path, 'r') as file:
            saved_data = json.load(file)
        keyname = "BaseModel." + new.id
        self.assertEqual(saved_data[keyname], self.storage.all()[keyname].to_dict())

    def test_reload_no_file(self):
        """Test reload method with no file"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        self.storage.reload()
        self.assertEqual(self.storage.all(), {})

    def test_reload_invalid_file(self):
        """Test reload method with invalid file content"""
        with open(self.file_path, "w") as f:
            f.write("Invalid JSON")
        self.storage.reload()
        self.assertEqual(self.storage.all(), {})


if __name__ == "__main__":
    unittest.main()#!/usr/bin/python3
"""Unit tests for FileStorage class"""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models
import json
import os


class MyFileStorageTest(unittest.TestCase):

    def setUp(self):
        """Set up for each test"""
        self.storage = FileStorage()
        self.file_path = FileStorage.get_file_path()

        # Clean up the file before each test
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def tearDown(self):
        """Tear down after each test"""
        # Clean up the file after each test
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        self.storage.get_objects().clear()  # Clear objects dictionary

    def test_file_storage_init(self):
        """Test initialization and class attributes"""
        filepath = FileStorage.get_file_path()
        _objs = self.storage.get_objects()  # Access objects via instance
        self.assertEqual(filepath, "file.json")
        self.assertIsInstance(filepath, str)
        self.assertIsInstance(_objs, dict)

    def test_base_model_methods(self):
        """Test methods of BaseModel"""
        new = BaseModel()
        self.assertTrue(hasattr(new, "__init__"))
        self.assertTrue(hasattr(new, "__str__"))
        self.assertTrue(hasattr(new, "save"))
        self.assertTrue(hasattr(new, "to_dict"))

    def test_all(self):
        """Test all method"""
        new = BaseModel()
        self.storage.new(new)
        self.assertIsInstance(self.storage.all(), dict)
        self.assertNotEqual(self.storage.all(), {})

    def test_new(self):
        """Test new method"""
        new = BaseModel()
        self.storage.new(new)
        keyname = "BaseModel." + new.id
        self.assertIsInstance(self.storage.all()[keyname], BaseModel)
        self.assertEqual(self.storage.all()[keyname], new)
        self.assertIn(keyname, self.storage.all())
        self.assertTrue(self.storage.all()[keyname] is new)

    def test_save(self):
        """Test save method"""
        new = BaseModel()
        self.storage.new(new)
        self.storage.save()
        with open(self.file_path, 'r') as file:
            saved_data = json.load(file)
        keyname = "BaseModel." + new.id
        self.assertIn(keyname, saved_data)
        self.assertEqual(saved_data[keyname], new.to_dict())

    def test_reload(self):
        """Test reload method"""
        new = BaseModel()
        self.storage.new(new)
        self.storage.save()
        self.storage.all().clear()
        self.storage.reload()
        with open(self.file_path, 'r') as file:
            saved_data = json.load(file)
        keyname = "BaseModel." + new.id
        self.assertEqual(saved_data[keyname], self.storage.all()[keyname].to_dict())

    def test_reload_no_file(self):
        """Test reload method with no file"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        self.storage.reload()
        self.assertEqual(self.storage.all(), {})

    def test_reload_invalid_file(self):
        """Test reload method with invalid file content"""
        with open(self.file_path, "w") as f:
            f.write("Invalid JSON")
        self.storage.reload()
        self.assertEqual(self.storage.all(), {})


if __name__ == "__main__":
    unittest.main()
