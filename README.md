# EasyBar

**EasyBar** is a simple and useful Python library for printing progress bars in console. It allows a high level of customisation with simple identifiers, and applies on all mainstream platforms with no other dependency requirements (just pure Python).

```python
>>> from EasyBar import EasyBar
>>> bar = EasyBar(100)
>>> list(bar)  # Iterable
EasyBar: [████████            ] 40 / 100
```

It is realised in pure Python and works in any console supporting **ANSI Escape Characters**. This provides optimal control of your progress bar with a few simple parameters.

This module currently supports Python 3.9+.

## Installation

 - Install via pip

 ```shell
 pip install EasyBar
 ```
 
 - Install using setup file

 Alternatively you can clone the repo and manually run setup.py in the root directory.
 
 ```shell
 git clone https://github.com/Green0116/EasyBar.git
 cd EasyBar
 python setup.py install
 ```
 
## APIs

***class*** EasyBar.**EasyBar**(total, mode='default', prefix=None, display='█', fill:=' ', margin=2, boundary='[]', colour='default', bg_colour='default')

Create a new progress bar object.

 - total: Total number of times to be executed
 - mode: Percentage or fractional display of progress
 - prefix: Description of progress bar
 - display: Character used as bar body
 - fill: Character used for filling up empty space
 - margin: Margin space to the right
 - boundary: A pair of enclosing chars for the progress bar
 - colour: Text colour of the progress bar
 - bg_colour: Background colour of the bar

***class*** EasyBar.**NestBar**(tasks)

Create a NestedBar object, which recursively goes through all the tasks.

 - tasks: An iterable object containing all the tasks to be done