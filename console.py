#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    classes = {"BaseModel" : BaseModel}

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
        elif arg in self.classes.keys():
            new = self.classes[arg]()
            print(new.id)
            new.save()
        else:
            print("** class doesn't exist **")
            
    def do_show(self, arg):
        if not arg:
            print("** class name missing **")
        else:
            line = arg.split(' ')
            if line[0] not in self.classes.keys():
                print("** class doesn't exist **")
            elif len(line) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(line[0], line[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])



if __name__ == '__main__':
    HBNBCommand().cmdloop()