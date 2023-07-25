#!/usr/bin/python3
''' the entry point to the command interpreter '''


import cmd
from models.base_model import BaseModel
from models import storage
import shlex


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
                new_obj.save()
                print(new_obj.id)

            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        
        
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return

        elif len(args) == 1:
            print("** instance id missing **")
            return
        else:
            clsName = args[0]
            idName = args[1]
        if clsName != "BaseModel":
            print("** class doesn't exist **")
            return
        obj_rep = storage.all()
        c_id = f"{clsName}.{idName}"
        if c_id in obj_rep:
            print(obj_rep[c_id])
        else:
            print("** no instance found **")
            return

    def do_destroy(self, arg):

        args1 = arg.split()
        if len(args1) == 0:
            print("** class name missing **")
            return
        elif len(args1) == 1 and args1[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        elif len(args1) == 1 and args1[0] == "BaseModel":
            print("** instance id missing **")
            return
        else:
            clsName = args1[0]
            idName = args1[1]
            obj_rep = storage.all()
            c_id = f"{clsName}.{idName}"

            if c_id in obj_rep:
                del obj_rep[c_id]
                storage.save()
            else:
                print("** no instance found **")
                return

    def do_all(self, arg):

        all_inst = storage.all()
        str_list = []
        if len(arg) == 0:
            for key in all_inst.keys():
                str_list.append(str(all_inst[key]))
            print(str_list)
        elif arg:
            for key in all_inst.keys():
                if key.split(".")[0] == arg:
                    str_list.append(str(all_inst[key]))
            print(str_list)
        else:
            print("** class doesn't exist **")
            return

    def do_update(self, arg):
        
        arg_list = shlex.split(arg)

        if len(arg_list) == 0:
            print("** class name missing **")
            return
        elif len(arg_list) == 1:
            print("** instance id missing **")
            return
        elif len(arg_list) == 2:
            print("** attribute name missing **")
            return
        elif len(arg_list) == 3:
            print("** value missing **")
            return
        else:
            all_obj = storage.all()
            cls_Name = arg_list[0]
            obj_id = arg_list[1]
            attr_name = arg_list[2]
            try:
                attr_value = eval(arg_list[3])
            except Exception:
                attr_value = str(arg_list[3])

            if cls_Name != "BaseModel":
                print("** class doesn't exist **")
                return
            
            str_rep = f"{cls_Name}.{obj_id}"
            if str_rep not in all_obj:
                print("** no instance found **")
                return
            setattr(all_obj[str_rep], attr_name, attr_value)



if __name__ == '__main__':
    HBNBCommand().cmdloop()
