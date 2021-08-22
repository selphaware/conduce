from functools import reduce
import yaml
import json
from os.path import join as opj


# reduce dictionary calls to a single string with '.' delimitation
def reduce_get(cfg: dict, key: str):
    return reduce(lambda c, k: c[k], key.split('.'), cfg)


# class to read config as reduced string with '.' delimitation
class ConfigReader(object):
    def __init__(self, cfg: dict):
        self.cfg = cfg

    # get
    def get(self, key):
        return reduce_get(self.cfg, key)


# read config (yaml)
def read_yaml(
        config_name: str,
        root_path=""
):
    path_yaml = opj(root_path, config_name)
    yaml_dict = yaml.load(open(path_yaml), Loader=yaml.FullLoader)

    return ConfigReader(yaml_dict).get


# read config (json)
def read_json(
        config_name: str,
        root_path=""
):
    path_json = opj(root_path, config_name)
    json_dict = json.load(open(path_json))

    return ConfigReader(json_dict).get
