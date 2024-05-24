#!/usr/bin/python3
"""
Console module for interacting with the user via command line.
"""

import cmd
import re
import shlex
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City



def curly_braces_split(cmd_arg):
    """
    Split the curly braces to extract the id and attributes for the update method.

    Args:
        cmd_arg (str): The command argument string.

    Returns:
        tuple: A tuple containing the id and a dictionary of attributes.
    """
    braces_curly = re.search(r"\{(.*?)\}", cmd_arg)

    if braces_curly:
        comma_id = shlex.split(cmd_arg[:braces_curly.span()[0]])
        id = [i.strip(",") for i in comma_id][0]

        data_str = braces_curly.group(1)
        try:
            attr_dict = json.loads("{" + data_str + "}")
        except Exception:
            print("** invalid dictionary format **")
            return None, None
        return id, attr_dict
    else:
        commands = cmd_arg.split(",")
        if commands:
            try:
                id = commands[0]
            except Exception:
                return "", ""
            try:
                name_attr = commands[1]
            except Exception:
                return id, ""
            try:
                value_attr = commands[2]
            except Exception:
                return id, name_attr
            return f"{id}", f"{name_attr} {value_attr}"
        else:
            return "", ""


class HBNBCommand(cmd.Cmd):
    """
    Console class for handling commands and interactions in the HBNB environment.
    """
    prompt = "(hbnb) "
    classes_valid = ["BaseModel", "User", "Amenity",
                     "Place", "Review", "State", "City"]

    def line_empty(self):
        """
        Nothing to do when the line is empty.
        """
        pass

    def EOF_do(self, arg):
        """
        Exit the program when the EOF (Ctrl+D) signal is received.
        """
        return True

    def do_quit(self, arg):
        """
        Exit the program using the quit command.
        """
        return True

    def do_create(self, arg):
        """
        Create a new instance of a specified class and save it to the JSON file.

        Usage: create <class_name>
        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.classes_valid:
            print("** class doesn't exist **")
        else:
            instance_new = eval(f"{commands[0]}()")
            storage.save()
            print(instance_new.id)

    def do_show(self, arg):
        """
        Display the string representation of an instance.

        Usage: show <class_name> <id>
        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.classes_valid:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            entities = storage.all()

            key = "{}.{}".format(commands[0], commands[1])
            if key in entities:
                print(entities[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Delete an instance specified by the class name and id.

        Usage: destroy <class_name> <id>
        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.classes_valid:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            entities = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if key in entities:
                del entities[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Print the string representation of all instances or instances of a specific class.

        Usage: <class name>.all()
               <class name>.show()
        """
        entities = storage.all()

        commands = shlex.split(arg)

        if len(commands) == 0:
            for key, value in entities.items():
                print(str(value))
        elif commands[0] not in self.classes_valid:
            print("** class doesn't exist **")
        else:
            for key, value in entities.items():
                if key.split('.')[0] == commands[0]:
                    print(str(value))

    def do_count(self, arg):
        """
        Count and retrieve the number of instances of a specified class.

        usage: <class name>.count()
        """
        entities = storage.all()

        commands = shlex.split(arg)

        if arg:
            cls_nm = commands[0]

        count = 0

        if commands:
            if cls_nm in self.classes_valid:
                for entity in entities.values():
                    if entity.__class__.__name__ == cls_nm:
                        count += 1
                print(count)
            else:
                print("** invalid class name **")
        else:
            print("** class name missing **")

    def do_update(self, arg):
        """
        Update an instance by updating or adding an attribute (e.g., name, age, etc...).

        Usage: update <class_name> <id> <attribute_name> "<attribute_value>"
               update <class_name> <id> {"attribute_name": "attribute_value"}
        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.classes_valid:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            entities = storage.all()

            key = "{}.{}".format(commands[0], commands[1])
            if key not in entities:
                print("** no instance found **")
            elif len(commands) < 3:
                print("** attribute name missing **")
            elif len(commands) < 4:
                print("** value missing **")
            else:
                entity = entities[key]

                id, attr_dict = curly_braces_split(arg)

                if attr_dict:
                    for name_attr, value_attr in attr_dict.items():
                        setattr(entity, name_attr, value_attr)
                else:
                    name_attr = commands[2]
                    value_attr = commands[3]
                    try:
                        value_attr = eval(value_attr)
                    except Exception:
                        pass
                    setattr(entity, name_attr, value_attr)

                entity.save()

    def default(self, arg):
            """
            Handle default behavior for the cmd module when the input is invalid.
            """
            arg_list = arg.split('.')

            cls_nm = arg_list[0]

            command = arg_list[1].split('(')

            met_cmd = command[0]

            if len(command) > 1:
                cmd_arg = command[1].split(')')[0]
            else:
                cmd_arg = ""

            dict_method = {
                    'all': self.do_all,
                    'show': self.do_show,
                    'destroy': self.do_destroy,
                    'update': self.do_update,
                    'count': self.do_count
                    }

            if met_cmd in dict_method.keys():
                if met_cmd != "update":
                    return dict_method[met_cmd]("{} {}".format(cls_nm, cmd_arg))
                else:
                    if not cls_nm:
                        print("** class name missing **")
                        return
                    try:
                        entity_id, attr_dict = curly_braces_split(cmd_arg)
                    except Exception:
                        pass
                    try:
                        invoke = dict_method[met_cmd]
                        return invoke("{} {} {}".format(cls_nm, entity_id, attr_dict))
                    except Exception:
                        pass
            else:
                print("*** Unknown syntax: {}".format(arg))
                return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()
