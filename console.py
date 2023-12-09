#!/usr/bin/python3
"""console.py

The file that contains the functionality for the console
of the hbnb project.
"""
import cmd
import models
import shlex
from datetime import datetime
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """HBNBCommand

    A class that contains all the functionalities for the
    console of the AirBnB project.
    """
    prompt = "(hbnb) "
    allowed_classes = ['BaseModel', 'User']

    def do_quit(self, line):
        """Quit command to quit the program.
        """
        return True

    def do_EOF(self, line):
        """Quit command to quit the program.
        """
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel.
        """
        class_name = self.parseline(line)[0]
        if class_name is None:
            print('** class name missing **')
        elif class_name not in self.allowed_classes:
            print("** class doesn't exist **")
        else:
            new_obj = eval(class_name)()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, line):
        """Prints the string representation of an instance
based on the class name and id.
        """
        class_name = self.parseline(line)[0]
        arg = self.parseline(line)[1]
        if class_name is None:
            print('** class name missing **')
        elif class_name not in self.allowed_classes:
            print("** class doesn't exist **")
        elif arg == '':
            print('** instance id missing **')
        else:
            inst_data = models.storage.all().get(class_name + '.' + arg)
            if inst_data is None:
                print('** no instance found **')
            else:
                print(inst_data)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id.
        """
        class_name = self.parseline(line)[0]
        arg = self.parseline(line)[1]
        if class_name is None:
            print('** class name missing **')
        elif class_name not in self.allowed_classes:
            print("** class doesn't exist **")
        elif arg == '':
            print('** instance id missing **')
        else:
            key = class_name + '.' + arg
            inst_data = models.storage.all().get(key)
            if inst_data is None:
                print('** no instance found **')
            else:
                del models.storage.all()[key]
                models.storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances
based or not on the class name.
        """
        class_name = self.parseline(line)[0]
        objs = models.storage.all()
        if class_name is None:
            print([str(objs[obj]) for obj in objs])
        elif class_name in self.allowed_classes:
            keys = objs.keys()
            print([str(objs[key]) for key in keys if key.startswith(
                class_name
            )])
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name and id
by adding or updating attribute.
        """
        args = shlex.split(line)
        args_size = len(args)
        if args_size == 0:
            print('** class name missing **')
        elif args[0] not in self.allowed_classes:
            print("** class doesn't exist **")
        elif args_size == 1:
            print('** instance id missing **')
        else:
            key = args[0] + '.' + args[1]
            inst_data = models.storage.all().get(key)
            if inst_data is None:
                print('** no instance found **')
            elif args_size == 2:
                print('** attribute name missing **')
            elif args_size == 3:
                print('** value missing **')
            else:
                args[3] = self.analyze_parameter_value(args[3])
                setattr(inst_data, args[2], args[3])
                setattr(inst_data, 'updated_at', datetime.now())
                models.storage.save()

    def emptyline(self):
        """emptyline

        Do nothing when the promt is an emptyline.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
