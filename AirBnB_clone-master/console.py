#!/usr/bin/python3
"""
Command Interpreter
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import models
import shlex

classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
           'State': State, 'City': City, 'Amenity': Amenity, 'Review': Review}


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter
    """
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Exit the program\n"""
        return True

    def help_EOF(self):
        print("CTRL + D (EOF) to exit the program")

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def help_quit(self):
        print("Quit command to exit the program")

    def emptyline(self):
        """Doesn't execute anything"""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel\n"""
        if line is None or len(line) == 0:
            print("** class name missing **")
        else:
            if line in classes:
                line = line.split()
                new_inst = eval(line[0] + "()")
                new_inst.save()
                print(new_inst.id)
            else:
                print("** class doesn't exist **")

    def help_create(self):
        print("Usage: create <valid class name>")

    def do_show(self, line):
        """Prints the string representation of an instance\n"""
        if line is None or len(line) == 0:
            print("** class name missing **")
        else:
            line = line.split(" ")
            if line[0] in classes:
                if len(line) < 2:
                    print("** instance id missing **")
                else:
                    key = str(line[0]) + "." + str(line[1])
                    obj = models.storage.all()
                    if key in obj:
                        print(obj[key])
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def help_show(self):
        print("Usage: show <valid class name> <valid id>")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id\n"""
        if line is None or len(line) == 0:
            print("** class name missing **")
        else:
            line = line.split(" ")
            if line[0] in classes:
                if len(line) < 2:
                    print("** instance id missing **")
                else:
                    key = str(line[0]) + "." + str(line[1])
                    obj = models.storage.all()
                    if key in obj:
                        del (obj[key])
                        models.storage.save()
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def help_destroy(self):
        print("Usage: destroy <valid class name> <valid id>")

    def do_all(self, line):
        """Prints all string representation of all instances\
based or not on the class name\n"""
        obj = models.storage.all()
        obj_list = []
        if line is "":
            for key in obj:
                obj_list.append(str(obj[key]))
            print(obj_list)
        else:
            try:
                line = line.split(" ")
                eval(line[0])
                for item in obj:
                    temp = obj[item].to_dict()
                    if temp['__class__'] == line[0]:
                        obj_list.append(str(obj[item]))
                print(obj_list)
            except Exception:
                print("** class doesn't exist **")

    def help_all(self):
        print("Usage: all OR all <valid class name>")

    def do_update(self, line):
        """Updates an instance based on the class name and id by\
            adding or updating attribute\n"""
        line = shlex.split(line)
        if len(line) == 0:
            print("** class name missing **")
        else:
            try:
                eval(str(line[0]))
            except Exception:
                print("** class doesn't exist **")
                return
            if len(line) == 1:
                print("** instance id missing **")
            else:
                objects = models.storage.all()
                key = str(line[0]) + "." + str(line[1])
                if key not in objects:
                    print("** no instance found **")
                else:
                    if len(line) == 2:
                        print("** attribute name missing **")
                    else:
                        if len(line) == 3:
                            print("** value missing **")
                        else:
                            setattr(objects[key], line[2], line[3])
                            models.storage.save()

    def help_update(self):
        print("Usage: update <valid class name>", end="")
        print("<valid id> <attribute name> <attribute value>")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
