#!/usr/bin/python3
"""
A module that test differents behaviors
of the class BaseModel
"""
import unittest
import pep8
from datetime import datetime
import time
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """TestBaseModel

    Tests if the BaseModel class works properly.
    """
    def test_pep8_base(self):
        """
        Test that checks PEP8
        """
        syntax = pep8.StyleGuide(quit=True)
        check = syntax.check_files(['models/base_model.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors (and warnings)."
        )

    def test_id_type(self):
        """
        Test that checks the type of the id attribute.
        """
        instance = BaseModel()
        self.assertEqual(type(instance.id), str)

    def test_id_unique(self):
        """
        Test that checks the id is unique for each instance.
        """
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_time_type_str(self):
        """
        Tests that the time attribute's type isn't of type string.
        """
        instance = BaseModel()
        self.assertNotEqual(type(instance.created_at), str)

    def test_time_type_datetime(self):
        """
        Tests that the time attribute's type is of type datetime.
        """
        instance = BaseModel()
        self.assertEqual(type(instance.created_at), datetime)

    def test_time_equal(self):
        """
        Tests that the `created_at` & `updated_at` are equal at the
        beginning.
        """
        instance = BaseModel()
        self.assertEqual(instance.created_at, instance.updated_at)

    def test_time_save(self):
        """
        Tests that the `created_at` & `updated_at` are different after
        saving.
        """
        instance = BaseModel()
        time.sleep(1)
        instance.save()
        self.assertNotEqual(instance.created_at, instance.updated_at)

    def test_str_print(self):
        """
        Tests the print of the overrided __str__ method
        """
        instance = BaseModel()
        string = "[{}] ({}) {}".format(
            instance.__class__.__name__,
            instance.id, instance.__dict__
        )
        self.assertEqual(str(instance), string)

    def test_to_dict_type(self):
        """
        Tests the type of the returning value of to_dict.
        """
        instance = BaseModel()
        var = instance.to_dict()
        self.assertEqual(type(var), dict)

    def test_to_dict_values(self):
        """
        Tests the value of the to_dict function.
        """
        instance = BaseModel()
        dictionary = instance.__dict__.copy()
        dictionary['__class__'] = instance.__class__.__name__
        dictionary['created_at'] = instance.created_at.isoformat()
        dictionary['updated_at'] = instance.updated_at.isoformat()
        self.assertEqual(dictionary, instance.to_dict())
