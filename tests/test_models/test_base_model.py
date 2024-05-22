#!/usr/bin/python3

import unittest
import uuid
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    ''' tests for the base model class '''

    def setUp(self):
        ''' setup for the test '''

        bm = BaseModel()
        bm.name = 'tested'
        bm.num = 20

    def test_init(self):
        ''' tests the init '''

        b = BaseModel()
        self.assertIsInstance(b.id, str)
        self.assertTrue(hasattr(b, 'created_at'))
        self.assertTrue(hasattr(b, 'updated_at'))

    def test_base_model_method(self):
        ''' checks if basemodel has methods '''

        self.assertTrue(hasattr(BaseModel, '__init__'))
        self.assertTrue(hasattr(BaseModel, '__str__'))
        self.assertTrue(hasattr(BaseModel, 'save'))
        self.assertTrue(hasattr(BaseModel, 'to_dict'))

    def test_base_model_id_is_string(self):
        '''
        test to check if the uuid is a string
        '''

        bm = BaseModel()
        self.assertIsInstance(bm.id, str)

    def test_base_model_diff_uuid(self):
        '''
        checks if uuid are different when using a
        different object
        '''

        bm_1 = BaseModel()
        bm_2 = BaseModel()
        c_uuid_1 = uuid.UUID(bm_1.id)
        c_uuid_2 = uuid.UUID(bm_2.id)
        self.assertNotEqual(c_uuid_1, c_uuid_2)

    def test_created_at_datetime(self):
        '''
        checks if created_at attr is set to th
        e current datetime the instance was cr        eated
        '''

        bm = BaseModel()
        created_at = bm.created_at
        self.assertIsInstance(bm.created_at, datetime)

    def test_update_at_datetime(self):
        '''
        checks if updated_at attr is updated to
        the current datetime the instance was
        created
        '''

        bm = BaseModel()
        updated_at = bm.updated_at
        self.assertIsInstance(bm.updated_at, datetime)

    def test_to_dict(self):
        ''' tests to_dict function '''

        obj = BaseModel()
        obj_dict = obj.to_dict()

        self.assertIn('__class__', obj_dict)
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)

        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['id'], obj.id)
        self.assertEqual(obj_dict['created_at'], obj.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], obj.updated_at.isoformat())

    def test_one_save(self):
        ''' tests the save method '''

        bm = BaseModel()
        f_updated_at = bm.updated_at

        bm.save()
        self.assertLess(f_updated_at, bm.updated_at)


if __name__ == '__main__':
    unittest.main()
