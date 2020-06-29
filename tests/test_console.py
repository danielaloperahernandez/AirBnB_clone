#!/usr/bin/python3
"""Unittests for console.py"""
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch

class Test_HBNBCommand(unittest.TestCase):
	def test_prompt(self):
		self.assertEqual("(hbnb) ", HBNBCommand.prompt)

	def test_help_EOF(self):
		text = "Handle End Of File"
		with patch('sys.stdout', new=StringIO()) as f:
			HBNBCommand().onecmd("help EOF")
			self.assertEqual(text, f.getvalue().strip())

	def test_help_quit(self):
		text = "Exit program"
		with patch('sys.stdout', new=StringIO()) as f:
			HBNBCommand().onecmd("help quit")
			self.assertEqual(text, f.getvalue().strip())

	def test_help_create(self):
		text = ("Creates a new instance of BaseModel, saves it (to the JSON file)\n        "
				"and prints the id. Ex: $ create BaseModel")
		with patch('sys.stdout', new=StringIO()) as f:
			HBNBCommand().onecmd("help create")
			self.assertEqual(text, f.getvalue().strip())

	def test_help_help(self):
		test_line1 = "Documented commands (type help <topic>):"
		test_line2 = "========================================"
		test_line3 = "Amenity    City  Place   State  all    create   help  show"
		test_line4 = "BaseModel  EOF   Review  User   count  destroy  quit  update"
		with patch('sys.stdout', new=StringIO()) as f:
			HBNBCommand().onecmd("help")
		line = f.getvalue()
		self.assertIn(test_line1, line)
		self.assertIn(test_line2, line)
		self.assertIn(test_line3, line)
		self.assertIn(test_line4, line)

	def test_space_notation(self):
		with patch('sys.stdout', new=StringIO()) as f:
			HBNBCommand().onecmd("create BaseModel")
			test_value = f.getvalue().strip()
		with patch('sys.stdout', new=StringIO()) as f:
			obj_test = storage.all()["BaseModel.{}".format(test_value)]
			command = "show BaseModel {}".format(test_value)
			HBNBCommand().onecmd(command)
			self.assertEqual(obj_test.__str__(), f.getvalue().strip())
		with patch('sys.stdout', new=StringIO()) as f:
			HBNBCommand().onecmd("create User")
			test_value = f.getvalue().strip()
		with patch('sys.stdout', new=StringIO()) as f:
			obj_test = storage.all()["User.{}".format(test_value)]
			command = "show User {}".format(test_value)
			HBNBCommand().onecmd(command)
			self.assertEqual(obj_test.__str__(), f.getvalue().strip())

	def test_show_missing_id_space(self):
		msg = "** instance id missing **"
		with patch('sys.stdout', new=StringIO()) as f:
			HBNBCommand().onecmd("show BaseModel")
		self.assertEqual(msg, f.getvalue().strip())
		with patch('sys.stdout', new=StringIO()) as f:
			HBNBCommand().onecmd("show User")
		self.assertEqual(msg, f.getvalue().strip())

	def test_show_missing_id_dot(self):
		msg = "** instance id missing **"
		with patch('sys.stdout', new=StringIO()) as f:
			HBNBCommand().onecmd("BaseModel.show()")
		self.assertEqual(msg, f.getvalue().strip())
		with patch('sys.stdout', new=StringIO()) as f:
			HBNBCommand().onecmd("User.show()")
		self.assertEqual(msg, f.getvalue().strip())

	def test_show_instance_no_found_space(self):
		msg = "** no instance found **"
		with patch('sys.stdout', new=StringIO()) as f:
			HBNBCommand().onecmd("show BaseModel 6767")
		self.assertEqual(msg, f.getvalue().strip())
		with patch('sys.stdout', new=StringIO()) as f:
			HBNBCommand().onecmd("show User 35353")
		self.assertEqual(msg, f.getvalue().strip())

	def test_show_instance_no_found_dot(self):
		msg = "** no instance found **"
		with patch('sys.stdout', new=StringIO()) as f:
			HBNBCommand().onecmd("BaseModel.show(4544)")
		self.assertEqual(msg, f.getvalue().strip())
		with patch('sys.stdout', new=StringIO()) as f:
			HBNBCommand().onecmd("User.show(5667)")
		self.assertEqual(msg, f.getvalue().strip())

	def test_show_class_name_missing(self):
		msg = "** class name missing **"
		with patch('sys.stdout', new=StringIO()) as f:
			HBNBCommand().onecmd("show")
		self.assertEqual(msg, f.getvalue().strip())
		with patch('sys.stdout', new=StringIO()) as f:
			HBNBCommand().onecmd("show")
		self.assertEqual(msg, f.getvalue().strip())