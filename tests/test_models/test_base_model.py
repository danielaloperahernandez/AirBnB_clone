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
        """Test save method"""
        base = BaseModel()
        date_now = datetime.now()
        self.assertEqual(date_now, base.save())

    def test_save_no_args(self):
        """Test save method without arguments"""
        with self.assertRaises(TypeError) as error:
            BaseModel.save()
        fail = "save() missing 1 required positional argument: 'self'"
        self.assertEqual(str(error.exception), fail)

    def test_save_many_args(self):
        """Test save method with many arguments"""
        with self.assertRaises(TypeError) as error:
            BaseModel.save(self, "holberton")
        fail = "save() takes 1 positional argument but 2 were given"
        self.assertEqual(str(error.exception), fail)

    def test_dict_no_args(self):
        """Test to_dict method without arguments"""
        with self.assertRaises(TypeError) as error:
            BaseModel.to_dict()
        fail = "to_dict() missing 1 required positional argument: 'self'"
        self.assertEqual(str(error.exception), fail)

    def test_dict_many_args(self):
        """Test to_dict method with many arguments"""
        with self.assertRaises(TypeError) as error:
            BaseModel.to_dict(self, "holberton")
        fail = "to_dict() takes 1 positional argument but 2 were given"
        self.assertEqual(str(error.exception), fail)

    def test_intantiation_dict_object(self):
        """Test instantiation"""
        base = BaseModel()
        base.number = 21
        base.dir = "74A"
        base_dict = base.to_dict()
        new_base = BaseModel(**base_dict)
        self.assertEqual(new_base.to_dict(), base.to_dict())

    def test_init_no_args(self):
        """Test instantiation without arguments"""
        with self.assertRaises(TypeError) as error:
            BaseModel.__init__()
        fail = "__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(error.exception), fail)

    def test_init_many_args(self):
        """Test instantiation with many arguments"""
        base = BaseModel(5, "hol", 12, "ber", 78, "ton")
        args = [a for a in range(245)]
        base = BaseModel(*args)

    def test_srt(self):
        """Test str method"""
        base = BaseModel()
        string = "[BaseModel] ({}) {}".format(base.id, base.__dict__)
        self.assertEqual(string, str(base))

if __name__ == '__main__':
    unittest.main()
