#!/usr/bin/python3
"""Test cases for FileStorage class"""
import unittest
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage

class TestFileStorage(unittest.TestCase):
	"""Test cases for the FileStorage class"""

	def setUp(self):
		"""Sets up test methods"""
		pass

	def tearDown(self):
		"""Tears down test methods"""
		pass

	def test_instantiation(self):
		"""Test instantiation of storage class"""
		self.assertEqual(type(storage).__name__, "FileStorage")

	def test_init_no_args(self):
		"""Test __init__ without arguments"""
		with self.assertRaises(TypeError) as error:
			FileStorage.__init__()
		fail = "descriptor '__init__' of 'object' object needs an argument"
		self.assertEqual(str(error.exception), fail)

	def test_init_many_args(self):
		"""Test __init__ with many arguments"""
		with self.assertRaises(TypeError) as error:
			base = FileStorage(67, 7, 12, 9, 4, 5)
		fail = "object() takes no parameters"
		self.assertEqual(str(error.exception), fail)

	def test_attributes(self):
		"""Test class attributes"""
		self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
		self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))

	def test_all(self):
		"""Test the all method"""
		storage = FileStorage()
		dict_new = storage.all()
		self.assertEqual(type(dict_new), dict)
		self.assertTrue(dict_new == {})

if __name__ == '__main__':
    unittest.main()

