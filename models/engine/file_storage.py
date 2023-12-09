#!/usr/bin/python3
"""file_storage.py
The FileStorage module file.
"""
import json
from os import path
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """class FileStorage

    Attributes:
        __file_path (str): The path to the JSON file.
        __objects (dict): A dictionary that will store all objects
                          by `<class name>.id`.
    """
    __file_path = "storage.json"
    __objects = {}

    def all(self):
        """all

        Returns the dictionary in __objects

        Return:
            (dict): The attribute __objects
        """
        return self.__objects

    def new(self, obj):
        """new

        Sets in `__objects` the new obj with key `<obj class name>.id`

        Attributes:
            obj (instance): The object to add in the `__objects` class
                            attribute.
        """
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """save

        Serializes `__objects` to the JSON file in `__file_path`.
        """
        json_dict = {}
        for k, v in self.__objects.items():
            json_dict[k] = v.to_dict()
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            f.write(json.dumps(json_dict))

    def reload(self):
        """reload

        Deserializes the JSON file in `__file_path` to `__objects` if the
        file existes otherwise do nothing.
        """
        if path.exists(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                json_dict = json.loads(f.read())
                for k, v in json_dict.items():
                    self.__objects[k] = eval(v['__class__'])(**v)
