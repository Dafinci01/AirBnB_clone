#!/usr/bin/python3
"""
Module for testing Review
"""
import os
import unittest
from datetime import datetime
from time import sleep
from models.review import Review
from models.base_model import BaseModel

class TestReview(unittest.TestCase):
    """
    Unittests for testing Review class.
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
        """Test instantiation of Review."""
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertIsInstance(review, BaseModel)

    def test_attributes(self):
        """Test attributes of Review."""
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertEqual(review.place_id, "")
        self.assertTrue(hasattr(review, "user_id"))
        self.assertEqual(review.user_id, "")
        self.assertTrue(hasattr(review, "text"))
        self.assertEqual(review.text, "")

    def test_id_is_unique(self):
        """Test that each Review instance has a unique ID."""
        review1 = Review()
        review2 = Review()
        self.assertNotEqual(review1.id, review2.id)

    def test_created_at_and_updated_at(self):
        """Test created_at and updated_at attributes."""
        review = Review()
        self.assertIsInstance(review.created_at, datetime)
        self.assertIsInstance(review.updated_at, datetime)

    def test_str_representation(self):
        """Test string representation of Review."""
        review = Review()
        review.id = "12345"
        review.text = "This is a test review."
        expected_str = f"[Review] ({review.id}) {review.__dict__}"
        self.assertEqual(str(review), expected_str)

    def test_save(self):
        """Test save() method."""
        review = Review()
        sleep(0.05)
        first_updated_at = review.updated_at
        review.save()
        self.assertLess(first_updated_at, review.updated_at)

    def test_to_dict(self):
        """Test to_dict() method."""
        review = Review()
        review.place_id = "12345"
        review.user_id = "67890"
        review.text = "This is a test review."
        review_dict = review.to_dict()
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertEqual(review_dict['place_id'], '12345')
        self.assertEqual(review_dict['user_id'], '67890')
        self.assertEqual(review_dict['text'], 'This is a test review.')
        self.assertIsInstance(review_dict['created_at'], str)
        self.assertIsInstance(review_dict['updated_at'], str)

if __name__ == '__main__':
    unittest.main()
