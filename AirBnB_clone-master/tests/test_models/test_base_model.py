#!/usr/bin/python3
"""
Basemodel Class Tests
"""

import unittest
import os
from models.base_model import BaseModel
from datetime import datetime


class BaseModelTest(unittest.TestCase):
    """
    Tests for BaseModel Class
    """

    @classmethod
    def setUpClass(cls):
        """ Setup an instance for test"""
        cls.my_model = BaseModel()
        cls.my_model.name = "David"
        cls.my_model.my_number = 89
        cls.my_model2 = BaseModel()
        cls.my_model2.name = "David"
        cls.my_model2.my_number = 89

    @classmethod
    def teardown(cls):
        """ Delete the instance at the end of tests"""
        del cls.my_model
        del cls.my_model2
        try:
            os.remove("file.json")
        except:
            pass

    def test_checking_for_docstring_BaseModel(self):
        """Test if all docstring were written"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_instance_BaseModel(self):
        """Test if my_model 1 and 2 are instances of BaseModel
        if are instances checks if the attributes were well
        assigned"""
        self.assertTrue(isinstance(self.my_model, BaseModel))
        self.assertTrue(isinstance(self.my_model2, BaseModel))
        self.assertEqual(self.my_model.name, "David")
        self.assertEqual(self.my_model2.name, "David")
        self.assertEqual(self.my_model.my_number, 89)
        self.assertEqual(self.my_model.my_number, 89)

    def test_diff_instances_BaseModel(self):
        """ Test if two instences were created at different time
        and have different id's"""
        self.assertNotEqual(self.my_model.id, self.my_model2.id)

    def test_str(self):
        """Test if __str__ method show the right output"""
        string = "[BaseModel] ({}) {}".format(self.my_model.id,
                                              self.my_model.__dict__)
        self.assertEqual(string, str(self.my_model))

    def test_save_BaseModel(self):
        """Test if updated at changes"""
        self.my_model.save()
        self.assertNotEqual(self.my_model.created_at, self.my_model.updated_at)

    def test_to_dict_BaseModel(self):
        """If the convertion to dictionary works:
        __class__: has to be created
        created_at and updated at have to change the format"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        model_dict = self.my_model.to_dict()
        self.assertEqual(self.my_model.__class__.__name__, 'BaseModel')
        self.assertEqual(type(model_dict['created_at']), str)
        self.assertEqual(type(model_dict['updated_at']), str)
        self.assertEqual(model_dict["created_at"],
                         self.my_model.created_at.strftime(t_format))
        self.assertEqual(model_dict["updated_at"],
                         self.my_model.updated_at.strftime(t_format))

    def test_from_dict_to_BaseModel(self):
        """Test if we can create an instance from a dictionary"""
        my_model_json = self.my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertTrue(isinstance(my_new_model, BaseModel))
        self.assertEqual(my_new_model.name, "David")
        self.assertEqual(my_new_model.my_number, 89)
        self.assertEqual(my_new_model.id, self.my_model.id)
        self.assertEqual(my_new_model.created_at, self.my_model.created_at)
        self.assertEqual(my_new_model.updated_at, self.my_model.updated_at)
        self.assertNotEqual(my_new_model, self.my_model)

if __name__ == '__main__':
    unittest.main()
