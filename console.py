#!/usr/bin/python3
"""console.py

The file that contains the functionality for the console
of the hbnb project.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """HBNBCommand

    A class that contains all the functionalities for the
    console of the AirBnB project.
    """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to quit the program.
        """
        return True

    def do_EOF(self, line):
        """Quit command to quit the program.
        """
        return True

    def emptyline(self):
        """emptyline

        Do nothing when the promt is an emptyline.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
