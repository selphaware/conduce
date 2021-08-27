from functools import reduce
import yaml
import json
from os.path import join as opj


# reduce dictionary calls to a single string with '.' delimitation
def reduce_get(cfg: dict, key: str):
    """
    gets value from dictionary based on flat 'key' provided
    e.g. instead of dict1["alpha"]["beta"]["gamma"], we do: key = "alpha.beta.gamma"
    :param cfg: config dictionary
    :param key: flat key e.g. "alpha.beta.gamma"
    :return: value from dictionary
    """
    return reduce(lambda c, k: c[k], key.split('.'), cfg)


# class to read config as reduced string with '.' delimitation
class ConfigReader(object):
    def __init__(self, cfg: dict):
        """
        constructor
        :param cfg: config dictionary
        """
        self.cfg = cfg

    # get
    def get(self, key: str = ""):
        """
        get value from dictionary based on flat key
        :param key: flat key e.g. "alpha.beta.gamma"
        :return: value from dictionary
        """
        return self.cfg if not len(key) else reduce_get(self.cfg, key)


# read config (general)
def read_config(
        config_type: str,
        config_name: str,
        root_path="",
        nstruct=False
):
    """
    general config reader
    :param config_type: json or yaml
    :param config_name: yaml/json file name
    :param root_path: yaml/json file path
    :param nstruct: True if return obj is NStruct otherwise is ConfigReader
    :return: ConfigReader object containing config
    """
    config_path = opj(root_path, config_name)
    config_fun = {
        "json": [json.load, {}],
        "yaml": [yaml.load, {"Loader": yaml.FullLoader}]
    }
    fun = config_fun[config_type]
    config_stream = open(config_path)
    config_dict = fun[0](config_stream, **fun[1])
    config_stream.close()

    return ConfigReader(config_dict).get if not nstruct else NStruct(**config_dict)


# read config (yaml)
def read_yaml(
        config_name: str,
        root_path="",
        nstruct=False
):
    """
    read yaml config into ConfigReader object
    :param config_name: yaml file name
    :param root_path: yaml file path
    :param nstruct: True if return obj is NStruct otherwise is ConfigReader
    :return: ConfigReader object
    """
    return read_config(config_type="yaml", config_name=config_name, root_path=root_path, nstruct=nstruct)


# read config (json)
def read_json(
        config_name: str,
        root_path="",
        nstruct=False
):
    """
    read json config into ConfigReader object
    :param config_name: json file name
    :param root_path: json file path
    :param nstruct: True if return obj is NStruct otherwise is ConfigReader
    :return: ConfigReader object
    """
    return read_config(config_type="json", config_name=config_name, root_path=root_path, nstruct=nstruct)


# Nested Structure class to hold contents of a dictionary
class NStruct:
    def __init__(self, **entries):
        """
        constructor which takes a dictionary and places all elements in this class
        :param entries: dictionary of key value pair items
        """
        for key, val in entries.items():
            if isinstance(val, dict):  # convert dic to NStruct obj
                self.__dict__.update({key: NStruct(**val)})
            elif isinstance(val, list):  # traverse through list converting dic's to NStruct
                self.__dict__.update({key: traverse_list(val, NStruct)})
            else:  # neither dic or list, set value to key
                self.__dict__.update({key: val})

    def value(self):
        """
        :return: returns full dictionary of current NStruct items
        """
        res = {}
        for k, v in self.__dict__.items():
            if isinstance(v, NStruct):  # traverse through NStruct, converting to dic
                res[k] = traverse_nstruct(v.__dict__)
            elif isinstance(v, list):  # traverse through list, converting NStruct to dic
                res[k] = traverse_list(v, dict)
            else:  # neither NStruct or list, set value to key
                res[k] = v
        return res


def traverse_list(lss: list, obj_type) -> list:
    """
    traverses through list converting dictionaries to NStruct
    :param lss: input list
    :param obj_type: either NStruct or dict
    :return: returns transformed list where dics are converted to NStruct
    """
    res = []
    for ls in lss:
        if isinstance(ls, dict):  # convert dic to obj_type (NStruct)
            if not (obj_type == NStruct):
                raise ValueError("Current item in list is a dict, "
                                 "therefore obj_type should be NStruct. "
                                 "Please contact support to resolve this matter.")
            res.append(obj_type(**ls))
        elif isinstance(ls, NStruct):  # convert NStruct to dic
            res.append(traverse_nstruct(ls.__dict__))
        elif isinstance(ls, list):  # traverse through list converting to obj_type = either dic or NStruct
            res.append(traverse_list(ls, obj_type))
        else:
            res.append(ls)
    return res


def traverse_nstruct(dic: dict) -> dict:
    """
    traverses through list converting NStruct to dictionaries
    :param dic: input list
    :return: returns transformed list where dics are converted to NStruct
    """
    res = {}
    for k, v in dic.items():
        if isinstance(v, NStruct):
            res[k] = traverse_nstruct(v.__dict__)
        elif isinstance(v, list):
            res[k] = traverse_list(v, dict)
        else:
            res[k] = v
    return res
