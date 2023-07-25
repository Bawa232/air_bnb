#!/usr/bin/python3
''' defining filestorage class '''



import json


class FileStorage:


    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        oclasname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(oclasname, obj.id)] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        Save/serialize obj dictionaries to json file
        """
        obj_dict = {}
        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review
        objde = {}
        try:
            with open(FileStorage.__file_path, 'r') as f:
                objde = json.load(f)

                for key, value in objde.items():
                    if value["__class__"] == "BaseModel":
                        FileStorage.__objects[key] = BaseModel(**value)
                    elif value["__class__"] == "User":
                        FileStorage.__objects[key] = "User"(**value)
                    elif value["__class__"] == State:
                        FileStorage.__objects[key] = "State"(**value)
                    elif value["__class__"] == City:
                        FileStorage.__objects[key] = "City"(""value)
                    elif value["__class__"] == "Place":
                        FileStorage.__objects[key] = Place(**value)
                    elif value["__class__"] == "Amenity":
                        FileStorage.__objects[key] = Amenity(**value)
                    elif value["__class__"] == "Review":
                        FileStorage.__objects[key] = Review(**value)
        except FileNotFoundError:
            pass
