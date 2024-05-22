#!/usr/bin/python3
"""This file is to test that the console is working (Console.py file)
Unit tests for the HBNBCommand class."""

import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
import console
from models.base_model import BaseModel
from models import storage


class MyHBNBCommandTest(unittest.TestCase):

    def setUp(self):
        """Set up for each test."""
        self.console = console.HBNBCommand()
        self.storage = storage

    def tearDown(self):
        """Tear down after each test."""
        self.storage.all().clear()

    def test_create(self):
        """Test the create command."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("create BaseModel")
            output = fake_out.getvalue().strip()
            self.assertTrue(len(output) > 0)
            self.assertIn("BaseModel." + output, self.storage.all())

    def test_show(self):
        """Test the show command."""
        instance = BaseModel()
        self.storage.new(instance)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(f"show BaseModel {instance.id}")
            output = fake_out.getvalue().strip()
            self.assertIn(instance.id, output)

    def test_destroy(self):
        """Test the destroy command."""
        instance = BaseModel()
        self.storage.new(instance)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(f"destroy BaseModel {instance.id}")
            self.assertNotIn("BaseModel." + instance.id, self.storage.all())

    def test_all(self):
        """Test the all command."""
        instance = BaseModel()
        self.storage.new(instance)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("all BaseModel")
            output = fake_out.getvalue().strip()
            self.assertIn(instance.id, output)

    def test_update(self):
        """Test the update command."""
        instance = BaseModel()
        self.storage.new(instance)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd(f'update BaseModel {instance.id} name "Test"')
            self.assertEqual(
                self.storage.all()[f"BaseModel.{instance.id}"].name,
                "Test"
            )

    def test_update_dict(self):
        """Test the update command with a dictionary."""
        instance = BaseModel()
        self.storage.new(instance)
        s_dict = '{"name": "Test", "number": 89}'
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.update_dict("BaseModel", instance.id, s_dict)
            self.assertEqual(
                self.storage.all()[f"BaseModel.{instance.id}"].name,
                "Test"
            )
            self.assertEqual(
                self.storage.all()[f"BaseModel.{instance.id}"].number,
                89
            )

    def test_quit(self):
        """Test the quit command."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("quit")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "")

    def test_EOF(self):
        """Test the EOF command."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("EOF")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "")

    def test_emptyline(self):
        """Test the emptyline command."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console.onecmd("")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "")


if __name__ == '__main__':
    unittest.main()
