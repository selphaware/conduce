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
```` 
<br><b>example.py</b>: <br>
````python 
from conduce import conduce
c1 = conduce.read_yaml("some.yaml", "some/path/to/the/yaml")
c2 = conduce.read_json("some.json", "some/path/to/the/json")
c3 = conduce.read_yaml("some_deep_nested.yaml", "some/path/to/the/yaml")
c1('alpha.beta.gamma') # returns value "hello"
c2('alpha.beta.gamma') # returns value "world"
c3('alpha.beta.gamma.delta.theta.phi') # returns value "finally!!!"
```` 
