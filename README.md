# Config (YAML/JSON) Keys Flatten-Reducer
<i><b>conduce</b></i> - A simple config package which flatten-reduces all keys of either a YAML or JSON config
to allow a simple way to get values from long keys.
<br><br>
<b>Installation</b><br>
````commandline
pip install conduce
````
<br><b>some.yaml</b>
````yaml 
alpha:
    beta:
        gamma: "hello"
```` 
<br><b>some.json</b>:<br>
````json 
{"alpha": {"beta": {"gamma": "world"}}}
```` 
<br><b>some_deep_nested.yaml</b>:<br>
````yaml 
alpha:
    beta:
        gamma:
            delta:
                theta:
                    phi:
                        "finally!!!"
    hello:
        - 1
        - 2
        - 3
        - rho:
            - 10
            - 100
            - fellow: "end of the road"
```` 
<br><b>example.py</b> reading YAML/JSON into ConfigReader: <br>
````python 
from conduce import conduce
# read config with nstruct=False as default for ConfigReader conversion
c1 = conduce.read_yaml(config_name="some.yaml", root_path="some/path/to/the/yaml")
c2 = conduce.read_json(config_name="some.json", root_path="some/path/to/the/json")
c3 = conduce.read_yaml(config_name="some_deep_nested.yaml", root_path="some/path/to/the/yaml")
c4 = conduce.read_config(config_type="json", config_name="some.json", root_path="some/path/to/the/yaml")

# get values
c1('alpha.beta.gamma') # returns value "hello"
c2('alpha.beta.gamma') # returns value "world"
c3('alpha.beta.gamma.delta.theta.phi') # returns value "finally!!!"
c4('alpha.beta.gamma') # returns value "world" (same as c2)
c4() # empty key returns full config dictionary of some.json
````

<br><b>example2.py</b> reading YAML/JSON into NStruct: <br>

`````python
from conduce import conduce
# NStruct (class object) example
c5 = conduce.read_yaml(config_name="some_deep_nested.yaml", 
                       root_path="some/path/to/the/yaml",
                       nstruct=True)  # set nstruct=True for NStruct
                                      # set nstruct=False for ConfigReader

c5.alpha.hello[3].rho[2].fellow # returns value "end of the road"
c5.value() # returns the full config dictionary
c5.alpha.hello[3].value() # returns the full dictionary of "rho"
`````

<br><b>example3.py</b> converting dictionary into NStruct: <br>
````python
from conduce import conduce
ex_dict = {"a": 1, "b": {"c": [1, 2, {"d": 3}]}, "d": []}  # example dic
ex_obj = conduce.NStruct(**ex_dict)  # convert dict to NStruct
print(ex_obj.b.c[2].d)  # returns 3
print(ex_obj.value())  # returns whole ex_dict dictionary
````

<br><b>example4.py</b> converting dictionary into ConfigReader: <br>
````python
ex_dict = {"a": 1, "b": {"c": [1, 2, {"d": 3}]}, "d": []}  # example dic
ex_obj = conduce.ConfigReader(ex_dict).get  # convert dict to ConfigReader
print(ex_obj("b.c")[2]["d"])  # returns 3
print(ex_obj())  # returns whole ex_dict dictionary
````
<br><b>Function signatures:</b>
````python
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

# reduce dic calls to a single string with '.' delimitation  (ConfigReader)
def reduce_get(cfg: dict, key: str):
    """
    gets value from dictionary based on flat 'key' provided
    e.g. instead of dict1["alpha"]["beta"]["gamma"], we do: key = "alpha.beta.gamma"
    :param cfg: config dictionary
    :param key: flat key e.g. "alpha.beta.gamma"
    :return: value from dictionary
    """

def traverse_nstruct(dic: dict) -> dict:
    """
    traverses through list converting NStruct to dictionaries
    :param dic: input list
    :return: returns transformed list where dics are converted to NStruct
    """

def traverse_list(lss: list, obj_type) -> list:
    """
    traverses through list converting dictionaries to NStruct
    :param lss: input list
    :param obj_type: either NStruct or dict
    :return: returns transformed list where dics are converted to NStruct
    """
````
