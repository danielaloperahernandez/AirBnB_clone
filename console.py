#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage

classes = {"BaseModel" : BaseModel}

class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb)"

    def do_EOF(self, arg):
        """Handle End Of File"""
        return True

    def do_quit(self, arg):
        """Exit program"""
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        if not arg:
            print("** class name missing **")
        line = arg.split(' ')
        
        else:
            print("** class doesn't exist **")



if __name__ == '__main__':
    HBNBCommand().cmdloop()