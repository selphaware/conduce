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
<br><b>example.py</b>: <br>
````python 
from conduce import conduce
c1 = conduce.read_yaml(config_name="some.yaml", root_path="some/path/to/the/yaml")
c2 = conduce.read_json(config_name="some.json", root_path="some/path/to/the/json")
c3 = conduce.read_yaml(config_name="some_deep_nested.yaml", root_path="some/path/to/the/yaml")
c4 = conduce.read_config(config_type="json", config_name="some.json", root_path="some/path/to/the/yaml")
c1('alpha.beta.gamma') # returns value "hello"
c2('alpha.beta.gamma') # returns value "world"
c3('alpha.beta.gamma.delta.theta.phi') # returns value "finally!!!"
c4('alpha.beta.gamma') # returns value "world" (same as c2)
c4() # empty key returns full config dictionary of some.json

# NStruct (class object) example
c5 = conduce.read_yaml(config_name="some_deep_nested.yaml", 
                       root_path="some/path/to/the/yaml",
                       type_obj=True)
c5.alpha.hello[3].rho[2].fellow # returns value "end of the road"
```` 
