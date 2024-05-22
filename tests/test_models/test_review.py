#!/usr/bin/python3
""" This py file will make all the unit tests
for our class Review and its objects"""

import unittest
from models.review import Review
from datetime import datetime


class MyReviewTest(unittest.TestCase):

    def setUp(self):
        # In order to test our class we need to Initialize a Review instance
        self.review = Review()

    def test_review_attributes(self):
        """Test the attributes of our Review object"""

        attributes = ["id", "created_at", "updated_at", "place_id", "user_id", "text"]

        for attr in attributes:
            self.assertTrue(hasattr(self.review, attr))
            self.assertIsInstance(getattr(self.review, attr), (str, datetime))


if __name__ == '__main__':
    unittest.main()
