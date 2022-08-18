# Week 2
## Day 2:17 Aug 2022

### virtualenv
1. What is a virtualenv?

  virtualenv is a tool used to keep the dependencies used by the project seperately and isolate it from other virtual environmentsand base python.

2. What is the difference between installing something inside a virtualenv and
otherwise?

## Pip
1. What is a package manager / installer
  Package managers are tools for software developers to help them easily share and install software libraries and also for managing dependencies.
  Python Package Manager (PyPM) is a Python utility intended to simplify the tasks of locating, installing, upgrading and removing Python packages
2. Software repository
    
a. What are the available software repositories for Java, JavaScript, Python
.. etc

  C++: Boost ,
  Python: PyPi ,
  R: CRAN ,
  Java: Maven and SpringSource ,
  JavaScript: Scripteka and JSAN ,
  Node.JS: NPM ,
  Lua: LuaForge and LuaRocks ,
  PHP: Pear and Pecl ,
  Ruby: RubyGems 

b. What is Pypi  

    PyPI  (Python Package Index) is the software repository for the python programming language.
    
3. Create a Pypi compatible package for some toy Python code of yours

4. Demonstrate different ways of installing your Python package
  a. using requirements.txt
    ```
    $ pip install -r requirements.txt
    ```
b. using setup.py

5. What is the difference between the above two methods? Which one is preferred
over the other in what situations?

Requirements.txt is used to set up an  development environment.
It is used by the developers to prepare the development environment.

setup.py is used to create packages that can be redistributed .
It is used to install packages in the end user system.

6. Read about "site-packages". Find the difference between the contents of your
package in the site-packages directory and your development directory

7. Figure out the difference between a whl file format and other file types for Python
package

8. What is editable mode in a package installation?

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
    conda create -n [environment_name] python=x.x anaconda
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
    c. Create a poetry.lock without installing any package

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
    curl -sSL https://install.python-poetry.org | python3 - --uninstall
    curl -sSL https://install.python-poetry.org | POETRY_UNINSTALL=1 python3 -
    ```


## Black and Isort

Black is a code reformatting tool .It reformats the code to improve readability.Black reformats entire files in place
Isort is used to sort imports alphabetically, and automatically separated into sections and by type. 
1.What is a formatting tool

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
pip install isort
```
3.Write a sample program and get it formatted using black and isort

4.How do you check
  a. If the code is already formatted or not
  
  b. If all the imports are properly ordered
  c. if there are any unwanted imports in the program

## Mypy
1. Static vs Dynamic type checking 

    Static type checking is done without runing the program. 
    C, C++, Java are examples of statically typed languages.

    Dynamic type checking is done during the runtime.
    Python, Javascript, C# are examples of dynamically typed languages

2. What is a type checker ?

  A type checker checks whether the operands of an operator are of compatable types

3. Why we need one for Python ?

4. Write an example programs with static typing using mypy
5. mypy.ini
  a. What are the contents of this file
  b. Create mypy.ini and add it to your repo

## Pylint
1. What is Linting / Static Code analysis

Linting is the process of checking the code for basic stylistic mistakes. It doesn't verify whether the code works or not, it checks that the code looks as good as possible and is readable by others.
pylint is a tool for linting code.

2. Write an example program and run pylint over that file
3. pylintrc file
  a. What are the contents of this file
  b. Create pylintrc file and add to your repo

## Pytest
1. What is a unitest
2. Write few unit tests and run pytest
3. Get the report of those runs
a. Save the report
4. Write sample pytest fixtures
a. Reuse them inside uni tests
b. Reuse them inside other fixtures
5. Use temporary directories and files
6. What is conftest.py
a. Create a sample file
7. Mock objects
8. Catch raised Exceptions
