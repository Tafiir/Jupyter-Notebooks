# Jupyter Notebooks
A place to store my Jupyter notebooks. They are mainly physics exercises and data evaluations for lab reports.

## Contents
### PAP2.1/2.2
Second practical physics training.

## Usage
To run them you either need to put the contents of init.py on the beginning of each one, or do
```python
from init import *
init()
```
You also can put the following into an IPython startup script:
```python
import os,sys
sys.path.insert(1, 'Path\\To\\This\\Jupyter Notebooks\\Repo')
from init import *
init()
```
Some of them require scripts from my [python-scripts repo](https://github.com/Tafiir/python-scripts).
