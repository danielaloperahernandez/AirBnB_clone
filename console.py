#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
import models

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
        if len(arg) == 0:
            print("** class name missing **")
        else:
            try:
                cls = models.classes[arg]
            except KeyError:
                print("** class doesn't exist **")
            else:
                obj = cls()
                obj.save()
                print(obj.id)


    def do_show(self, arg):
        if len(arg) == 0:
            print("** class name missing **")
        else:
            line = arg.split(' ')
            if line[0] in models.classes:
                try:
                    key = "{}.{}".format(line[0], line[1])
                except IndexError:
                    print("** instance id missing **")
                else:
                    try:
                        print(models.storage.all()[key])
                    except KeyError:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")




                """print("** class doesn't exist **")
            elif len(line) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(line[0], line[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])"""

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if len(arg) == 0:
            print("** class name missing **")
        else:
            line = arg.split(' ')
            if line[0] in models.classes:
                try:
                    key = "{}.{}".format(line[0], line[1])
                except IndexError:
                    print("** instance id missing **")
                else:
                    try:
                        del models.storage.all()[key]
                    except KeyError:
                        print("** no instance found **")
                    else:
                        models.storage.save()
            else:
                print("** class doesn't exist **")


    def do_all(self, arg):
        if len(arg) == 0:
            print([str(value) for value in models.storage.all().values()])
        elif arg not in models.classes:
            print("** class doesn't exist **")
        else:
            print([str(value) for key, value in models.storage.all().items() if arg in key])

    def do_update(self, arg):
        if len(arg) == 0:
            print("** class name missing **")
        else:
            line = arg.split(' ')
            if line[0] in models.classes:
                try:
                    key = "{}.{}".format(line[0], line[1])
                except IndexError:
                    print("** instance id missing **")
                else:
                    try:
                        obj_upt = models.storage.all()[key]
                    except KeyError:
                        print("** no instance found **")
                    else:
                        try:
                            atrribute = line[2]
                        except IndexError:
                           print("** attribute name missing **")
                        else:
                            try:
                                value = line[3]
                            except IndexError:
                                print("** value missing **")
                            else:
                                setattr(obj_upt, atrribute, value)
                                obj_upt.save()
            else:
                print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()