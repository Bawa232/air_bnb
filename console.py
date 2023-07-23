#!/usr/bin/python3
''' the entry point to the command interpreter '''


import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_EOF(self, arg):
        ''' method to exit the cli with ctrl + d in linux
        and ctrl + c in windows '''

        return True

    def do_quit(self, arg):
        ''' method to quit the cli() '''

        return True

    def emptyline(self):
        pass

    def do_create(self, arg):

        if arg:
            if arg == 'BaseModel':
                new_obj = BaseModel()
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        
        if arg:
            args = arg.split()
            if len(args) == 0:
                print("** class name missing **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                clsName = args[0]
                idName = args[1]
if __name__ == '__main__':
    HBNBCommand().cmdloop()
