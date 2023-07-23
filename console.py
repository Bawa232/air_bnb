#!/usr/bin/python3
''' the entry point to the command interpreter '''


import cmd


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_EOF(self, line):
        ''' method to exit the cli with ctrl + d in linux
        and ctrl + c in windows '''

        return True

    def do_quit(self, line):
        ''' method to quit the cli() '''

        return True

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
