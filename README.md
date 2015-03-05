# ProceduralGrid

## Requirements
* Python 3.4
* Virtualenv

## Instalation
* Initializate the project
* Clone this repo in the project dir
* Activate the virtualenv
* Install requirements:
```bash
pip install -r etc/requirements.txt
```

## Unit tests
Tests are launched with py.test, because it rocks.

* *pytest-pep8* for syntax verify
* *pytest-pycharm* for enabling ipdb debug during tests
* *pytest-sugar* because I love candy
* *ipdb* for console live debugging

Launch tests from project root with command:
```bash
py.test . --tb=line -s
```

*Note:* The ```-s``` option enable print statements and ipdb breakpoints

