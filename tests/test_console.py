#!/usr/bin/python3
"""Unittests for console.py"""
import pep8
import os
import console
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class Test_HBNBCommand(unittest.TestCase):
    """Tests for the console"""

    @classmethod
    def setUpClass(cls):
        """setup for the test"""
        cls.consol = HBNBCommand()

    def tearDown(self):
        """Remove temporary file (file.json) created as a result"""
        FileStorage._FileStorage__objects = {}
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_console_pep8_conformance(self):
        """checks if the Console code is PEP8 conformant"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0)

    def test_docstrings_in_console(self):
        """checking for docstrings"""
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.do_count.__doc__)

    def test_prompt(self):
        """Tests if the prompt is the correct"""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_emptyline(self):
        """Test empty line input"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("\n")
            self.assertEqual('', f.getvalue())

    def test_help_EOF(self):
        """checks if the help cpmmand is working correctly"""
        text = "Handle End Of File"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            self.assertEqual(text, f.getvalue().strip())

    def test_help_quit(self):
        """checks if help cpmmand is working correctly with quit command"""
        text = "Exit program"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            self.assertEqual(text, f.getvalue().strip())

    def test_help_quit(self):
        """checks if help cpmmand is working correctly with create command"""
        text = ("Exit program")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            self.assertEqual(text, f.getvalue().strip())

    def test_help_help(self):
        """tests if the output of help command is correct"""
        line1 = "Documented commands (type help <topic>):"
        line2 = "========================================"
        line3 = "Amenity    City  Place   State  all    create   help  show"
        line4 = "BaseModel  EOF   Review  User   count  destroy  quit  update"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
        line = f.getvalue()
        self.assertIn(line1, line)
        self.assertIn(line2, line)
        self.assertIn(line3, line)
        self.assertIn(line4, line)
