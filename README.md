# Config (YAML) Reducer - a config util package

<b>some.yaml</b>:<br>
alpha:<br>
&nbsp;&nbsp;&nbsp;&nbsp;beta:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;gamma: \"hello\"<br><br>
<b>example.py</b>: <br>
from conduce import conduce <br>
cfg = conduce.read_config(\"some.yaml\", \"some/path/to/yaml\")<br>
cfg(\'alpha.beta.gamma\') &nbsp;&nbsp; # gives us \"hello\"

[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.