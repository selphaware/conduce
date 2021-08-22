from functools import reduce
import yaml
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


# read config
def read_config(
        config_name: str,
        root_path=""
):
    path_yaml = opj(root_path, config_name)
    yaml_dict = yaml.load(open(path_yaml), Loader=yaml.FullLoader)

    return ConfigReader(yaml_dict).get
