###TreasureHunt

*** 

To start you need to have installed python 3.7

Firstly create virtual environments for project
And activate it

```
python3.7 -m venv venv
source /venv/bin/activate
```

install packages from requirements.txt located at root path:

``pip install requirements.txt``
***

To run solution prompt command from the root path:

- for functional:
```
python solution_functional.py
```

- for object model:
```
python solution_object_model.py
```

It will ask you to prompt matrix NxN (5x5)
as five strings with numbers as bellow:
```
55 14 25 52 21
44 31 11 53 43
24 13 45 12 34
42 22 43 32 41
51 23 33 54 15
```

And script will raise exception in case if
input format is wrong or if there is a loop in map

***
To run tests create test run configuration in the IDE or
run next command from the root path:

```
pytest tests
```