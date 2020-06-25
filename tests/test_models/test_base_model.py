#!/usr/bin/python3
"""Test cases for BaseModel class"""

import unittest
import time
import pep8
import uuid
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    def setUp(self):
        """Set up test methods"""
        pass

    def tearDown(self):
        """Tear Down test methods"""
        pass

    def test_BaseModel_pep8(self):
        """pep8 test"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/base_model.py'])
        self.assertEqual(result.total_errors, 0)

    def test_instantiation(self):
        """Test instantiation of BaseModel class"""
        base = BaseModel()
        self.assertEqual(str(type(base)), "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(base, BaseModel)
        self.assertTrue(issubclass(type(base), BaseModel))
        self.assertEqual(type(base.created_at), datetime.datetime)
        self.assertTrue(type(base.updated_at), datetime.datetime)

    def test_instantiation_dict(self):
        """Test instantiation with **kwargs"""
        dic = {"__class__": "BaseModel",
               "updated_at": datetime(2021, 9, 28, 21, 3, 54, 52302).isoformat(),
               "created_at": datetime.now().isoformat(),
               "id": uuid.uuid4(),
               "name": "Rose",
               "mi_number": 67}
        obj = BaseModel(**dic)
        self.assertEqual(obj.to_dict(), dic)
        self.assertTrue(type(dic) is dict)

    """def test_instantiation_dict_empty(self):
        Test instantiation with **kwargs
        dic_empty = {}
        obj = BaseModel(**dic_empty)
        self.assertEqual(obj.to_dict(), dic_empty)
        self.assertTrue(type(dic_empty) is dict)"""

    def test_save(self):
        base = BaseModel()
        date_now = datetime.now()
        self.assertEqual(date_now, base.save())


if __name__ == '__main__':
    unittest.main()
