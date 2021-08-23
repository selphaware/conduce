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


# read config (general)
def read_config(
        config_type: str,
        config_name: str,
        root_path=""
):
    """
    general config reader
    :param config_type: json or yaml
    :param config_name: yaml/json file name
    :param root_path: yaml/json file path
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

    return ConfigReader(config_dict).get


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
    return read_config(config_type="yaml", config_name=config_name, root_path=root_path)


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
    return read_config(config_type="json", config_name=config_name, root_path=root_path)
