#!/usr/bin/python3
import json
from models.base_model import BaseModel
"""
class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances
"""
class FileStorage:
    """
    __file_path: string - path to the JSON file (ex: file.json)
    __objects: dictionary - empty but will store all objects by <class name>.id
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """return dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        data = {}
        for k, v in self.__objects.items():
            data[k] = v.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(data, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        data_dict = {}
        classes = {"BaseModel" : BaseModel}
        try:
            with open(self.__file_path, 'r') as f:
                data_dict = json.load(f)
                for k, v in data_dict.items():
                    self.__objects[k] = classes[v["__class__"]](**v)
        except FileNotFoundError:
            pass