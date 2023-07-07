#!/usr/bin/python3
"""Test of Place Class """

from models.place import Place
import datetime
import unittest


class TestPlace(unittest.TestCase):
    """ Test Place Class """
    model = Place()

    def test_checking_for_docstring(self):
        """Test if all docstring were written"""
        self.assertIsNotNone(Place.__doc__)

    def test_instance(self):
        """Test if my_model 1 and 2 are subclasses of BaseModel"""
        self.assertIsInstance(self.model, Place)

    def test_attribute_city_id(self):
        """ Tests attributes """
        self.assertEqual(hasattr(self.model, "city_id"), True)
        self.assertEqual(hasattr(self.model, "user_id"), True)
        self.assertEqual(hasattr(self.model, "name"), True)
        self.assertEqual(hasattr(self.model, "description"), True)
        self.assertEqual(hasattr(self.model, "number_rooms"), True)
        self.assertEqual(hasattr(self.model, "number_bathrooms"), True)
        self.assertEqual(hasattr(self.model, "max_guest"), True)
        self.assertEqual(hasattr(self.model, "price_by_night"), True)
        self.assertEqual(hasattr(self.model, "latitude"), True)
        self.assertEqual(hasattr(self.model, "longitude"), True)
        self.assertEqual(hasattr(self.model, "amenity_ids"), True)

    def test_type(self):
        """ test type """
        self.assertEqual(type(self.model.city_id), str)
        self.assertEqual(type(self.model.user_id), str)
        self.assertEqual(type(self.model.name), str)
        self.assertEqual(type(self.model.description), str)
        self.assertEqual(type(self.model.number_rooms), int)
        self.assertEqual(type(self.model.number_bathrooms), int)
        self.assertEqual(type(self.model.max_guest), int)
        self.assertEqual(type(self.model.price_by_night), int)
        self.assertEqual(type(self.model.latitude), float)
        self.assertEqual(type(self.model.longitude), float)
        self.assertEqual(type(self.model.amenity_ids), list)

if __name__ == '__main__':
    unittest.main()
