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
    def get(self, key):
        """
        get value from dictionary based on flat key
        :param key: flat key e.g. "alpha.beta.gamma"
        :return: value from dictionary
        """
        return reduce_get(self.cfg, key)


# read config (yaml)
def read_yaml(
        config_name: str,
        root_path=""
):
    """
    read yaml config into ConfigReader object
    :param config_name: yaml file name
    :param root_path: yaml file path
    :return: ConfigReader object
    """
    path_yaml = opj(root_path, config_name)
    yaml_dict = yaml.load(open(path_yaml), Loader=yaml.FullLoader)

    return ConfigReader(yaml_dict).get


# read config (json)
def read_json(
        config_name: str,
        root_path=""
):
    """
    read json config into ConfigReader object
    :param config_name: json file name
    :param root_path: json file path
    :return: ConfigReader object
    """
    path_json = opj(root_path, config_name)
    json_dict = json.load(open(path_json))

    return ConfigReader(json_dict).get
