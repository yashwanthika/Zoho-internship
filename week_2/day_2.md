# Week 2
## Day 2: 17 Aug 2022

### virtualenv
1. What is a virtualenv?

  virtualenv is a tool used to keep the dependencies used by the project seperately and isolate it from other virtual environments and base python.

2. What is the difference between installing something inside a virtualenv and
otherwise?

It is not possible to install two different versions of the smae library at the same time but both the versions may be needed for two different packages in this case virtualenv comes into rescue . A package inatalled inside a virtual environment is isolated from the other virtual enviroments and base python. while a package installed in base python can cause dependency issues when we require an other version of the same package for different project.



## Conda
1. Difference between Pip and Conda

Pip is a dependency management tool that comes together with the standard Python installation for Windows and can be installed via Homebrew for MacOS and the distribution app manager for Linux systems.The default repository it uses when you run pip install is the Python Package Index (PyPI).

Conda is a dependency management tool that comes with Anaconda.The default repository that conda uses when you run conda install is the Anaconda Distribution Repository


2. Install Conda/Miniconda

    ```
    $ bash Anaconda-latest-Linux-x86_64.sh
    ```
    Miniconda
    ```
    $ bash Miniconda3-latest-Linux-x86_64.sh
    ```

3. Create an environment

    ```
    $ conda create -n [environment_name] python=x.x anaconda
    ```

4. Activate the environment

    ```
    $ conda activate [environment_name]
    ```

5. Install any package inside the environment

    ```
    $ conda install -n [environment_name] [package_name]
    ```

6. List down the packages installed inside the environment

    ```
    $ conda list
    ```

7. Remove the package from the environment

    ```
    $ conda remove [package_name]
    ```

8. Deactivate the environment

    ```
    $ conda deactivate
    ```

9. Delete the environment

    ```
    $ conda env remove -n [environment_name]
    ```
    or
    ```
    $ conda env remove -p [environment_path]
    ```

10. Update Conda Version

    ```
    $ conda update conda
    ```

11. Uninstall Conda

    To remove miniconda
    ```
    $ rm -rf ~/miniconda
    ```
    To remove conda
    ```
    $ rm -rf ~/.condarc ~/.conda ~/.continuum
    ```

## Poetry
1. Why poetry?

    Poetry is a tool to handle dependency installation as well as building and packaging of Python packages.It helps us to declare, manage and install dependencies of Python projects.

2. Installation
    To install poetry either use 
    ```
    $ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
    ```
    or 

    ```
    $ pip install poetry
    ```
    a. Installing a specific version
    To install a specific version, --version option or the $POETRY_VERSION environment variable is used.
    ```
    $ curl -sSL https://install.python-poetry.org | python3 - --version 1.2.0
    $ curl -sSL https://install.python-poetry.org | POETRY_VERSION=1.2.0 python3 -
    ```

3. Update poetry version
    ```
    $ poetry self update
    ```
    To update specific version
    ```
    $ poetry self update [version]
    ```

4. Add dependency
    a. Add a package from github repo 
        ```
        $ poetry add git+[url]
        ```
        i. From a specific branch or tag or commit:
        ```
        poetry add git+[specific_url]
        ```
        Example
        ```
        poetry add git+https://github.com/sdispater/pendulum.git#develop
        poetry add git+https://github.com/sdispater/pendulum.git#2.0.5
        ```
        

    b. Add a package from a local path
     ```
     $ poetry add [package_path]
     ```
    c. Other possible ways to add a dependency
      To  add an editable dependency
      ```
      $ poetry add --editable [path]
      $ poetry add --editable git+[url]
      ```

5. Poetry lock file
    a. What is a poetry.lock file
    
    poetry.lock file contains the dependencies with their version to be installed.
    If there is no poetry.lock file ,the dependencies are resolved for the packages mentioned in the pyproject.toml file and gets downloaded .These dependencies along with their version are written in the poetry.lock file such that the project is locked to those specific versions.
    
    
    b. Create a poetry.lock and install the dependencies (inside a conda env)
    ![poetry_lock_example](https://github.com/yashwanthika/Zoho-internship/blob/main/week_2/images/Poetry_lock.png)
    
    c. Create a poetry.lock without installing any package
    
    `$ poetry add [packagename]` updates the lock file or creates one if it is not present .
    poetry install is used to install the dependecies as per the lock file

6. Update dependencies
    ```
    $ poetry update
    ```
    This will fetch the latest versions for the dependencies mentioned in the pyproject.toml file and updates the lock file to the latest versions

7. Show poetry config
    ```
    $ poetry show
    ```
8. Modify poetry config values
    ```
    $ poetry config [options] [setting-key] [setting-value1] ... [setting-valueN]
    ```
    options:
    --list  - list the configurations
    --unset - remove the configuration of that specific key
9. Uninstall poetry
    ```
    $ curl -sSL https://install.python-poetry.org | python3 - --uninstall
    $ curl -sSL https://install.python-poetry.org | POETRY_UNINSTALL=1 python3 -
    ```


## Black and Isort

Black is a code reformatting tool .It reformats the code to improve readability.Black reformats entire files in place
Isort is used to sort imports alphabetically, and automatically separated into sections and by type. 

1.What is a formatting tool

Formatting tool is used to beautify the code and make it more human readable .Automatic code styling can potentially reduce bugs.
The most popular Python formatters are:
Black,
isort,
autopep8,
YAPF.
2.Install black and isort
Installation of black
```
$ pip install black
```
Installation of isort 
```
$ pip install isort
```
3.Write a sample program and get it formatted using black and isort
```
import numpy as np
import sys

  
def addition(a   ,       b):
    ans=a+      b
    
    return ans
    
def subtraction(a   ,       b):
    ans=a      -      b
    return ans
from numpy import arange,argmax
a = arange(5)
print(a)
print(argmax(a))
```

Using Black

![](https://github.com/yashwanthika/Zoho-internship/blob/main/week_2/images/black.png)
![](https://github.com/yashwanthika/Zoho-internship/blob/main/week_2/images/black_formatted_code.png)

Using isort

![](https://github.com/yashwanthika/Zoho-internship/blob/main/week_2/images/isort_cmd.png)
![](https://github.com/yashwanthika/Zoho-internship/blob/main/week_2/images/isort_formatted_code.png)

4.How do you check
  a. If the code is already formatted or not
  ```
  $ black --check --target-version=py35 .
  ```
  --check option can be used to know whether the code needs any further formatting or it is already good to go.
  
  b. If all the imports are properly ordered
  isort can also be used to verify that code is correctly formatted by running it with -c
  ```
  $ isort [filename].py -c
  ```
  c. if there are any unwanted imports in the program
  
  unwanted imports cant be removed by black or isort. Autoflake can be used to remove unwanted imports
