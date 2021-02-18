from pathlib import Path
import json

BASE_PATH = Path(__file__).parent


def open_json(path):
    with open(path, 'r') as file:
        return json.load(file)


def save2json(path, data):
    with open(path, 'w') as file:
        return json.dump(data, file)


class ConfigDescriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, obj, type=None) -> object:
        return obj.__dict__.get(self.name)

    def __set__(self, obj, value) -> None:
        obj.__dict__[self.name] = value
        data = open_json(obj.CONFIG_PATH)
        data.update({self.name: value})
        save2json(obj.CONFIG_PATH, data)


class ConfigMeta(type):
    """config singleton"""
    _instances = {}

    def __new__(cls, name, bases, clsdict):
        clsobj = super().__new__(cls, name, bases, clsdict)
        for name, value in open_json(clsobj.CONFIG_PATH).items():
            setattr(clsobj, name,  ConfigDescriptor(name))
        return clsobj

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(ConfigMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Config(metaclass=ConfigMeta):
    CONFIG_PATH = BASE_PATH / 'config.json'

    def __init__(self):
        for name, value in open_json(self.CONFIG_PATH).items():
            self.__setattr__(name, value)



config = Config()
