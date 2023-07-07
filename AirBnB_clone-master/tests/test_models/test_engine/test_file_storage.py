#!/usr/bin/python3
"""
File storage Class Tests
"""

import unittest
import os
from models.base_model import BaseModel
from models.state import State
from models.engine.file_storage import FileStorage
from datetime import datetime
import json


class FileStorageTest(unittest.TestCase):
    """
    Tests for BaseModel Class
    """

    @classmethod
    def setUpClass(cls):
        """ Setup an instance for test"""
        cls.my_model = BaseModel()
        cls.my_model.name = "Holberton"
        cls.my_model.my_number = 89

    @classmethod
    def teardown(cls):
        """ Delete the instance at the end of tests"""
        del cls.my_model
        try:
            os.remove("file.json")
        except:
            pass

    def test_checking_for_docstring_FileStorage(self):
        """ Test if all docstring were written"""
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_isattribute_FileStorage(self):
        """Checks if __objects and __file_path are att of FileS"""
        self.assertTrue(hasattr(FileStorage, '_FileStorage__objects'))
        self.assertTrue(hasattr(FileStorage, '_FileStorage__file_path'))

    def test_all_FileStorage(self):
        """ Test if 'all' method is working good """
        storage = FileStorage()
        all_objects = storage.all()
        self.assertEqual(type(all_objects), dict)
        self.assertIsNotNone(all_objects)
        self.assertIs(all_objects, storage._FileStorage__objects)
        key = self.my_model.__class__.__name__ + "." + self.my_model.id
        print_obj = all_objects[key]
        string = "[BaseModel] ({}) {}".format(self.my_model.id,
                                              self.my_model.__dict__)
        self.assertEqual(string, str(print_obj))

    def test_new_FileStorage(self):
        """ Test if 'new' method is working good """
        storage = FileStorage()
        all_objects = storage.all()
        my_model2 = State()
        my_model2.name = "Bogota D.C."
        storage.new(my_model2)
        self.assertEqual(type(all_objects), dict)
        self.assertIsNotNone(all_objects)
        self.assertIs(all_objects, storage._FileStorage__objects)
        key = my_model2.__class__.__name__ + "." + my_model2.id
        self.assertIsNotNone(all_objects[key])
        print_obj = all_objects[key]
        string = "[State] ({}) {}".format(my_model2.id,
                                          my_model2.__dict__)
        self.assertEqual(string, str(print_obj))

    def test_save_FileStorage(self):
        """ Test if 'new' method is working good """
        var1 = self.my_model.to_dict()
        new_key = var1['__class__'] + "." + var1['id']
        storage = FileStorage()
        storage.save()
        with open("file.json", 'r') as fd:
            var2 = json.load(fd)
        new = var2[new_key]
        for key in new:
            self.assertEqual(var1[key], new[key])

    def test_new(self):
        """testing change len """
        storage = FileStorage()
        l1 = len(storage.all())
        new = BaseModel()
        storage.save()
        storage.reload()
        l2 = len(storage.all())
        self.assertEqual(l1, l2 - 1)

if __name__ == '__main__':
    unittest.main()
