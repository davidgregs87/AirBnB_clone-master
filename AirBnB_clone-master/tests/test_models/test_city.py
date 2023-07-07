#!/usr/bin/python3
"""Test of City Class """

from models.city import City
import unittest


class TestCity(unittest.TestCase):
    """ Test City Class """
    model = City()

    def test_checking_for_docstring_User(self):
        """Test if all docstring were written"""
        self.assertIsNotNone(City.__doc__)

    def test_subclass_instance_User(self):
        """Test if my_model 1 and 2 are subclasses of BaseModel"""
        self.assertIsInstance(self.model, City)

    def test_attribute(self):
        """ Tests attributes """
        self.assertEqual(hasattr(self.model, "state_id"), True)
        self.assertEqual(hasattr(self.model, "name"), True)

    def test_types(self):
        """ test types """
        self.assertEqual(type(self.model.state_id), str)
        self.assertEqual(type(self.model.name), str)

if __name__ == '__main__':
    unittest.main()
