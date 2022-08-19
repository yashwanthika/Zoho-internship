# Week 2
# Day:3 18 AUG 2022

## Pip
1. What is a package manager / installer

  Package managers are tools for software developers to share and install software libraries and also for managing dependencies.
  Python Package Manager (PyPM) is a Python utility intended to simplify the tasks of locating, installing, upgrading and removing Python packages.
  
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

3. Demonstrate different ways of installing your Python package
  a. using requirements.txt
  It is used in development environment and contains the necessary packages needed for a project.
    ```
    $ pip install -r requirements.txt
    ```
b. using setup.py

It is used in packages.It is a python script typically included in the Python written libraries

4. What is the difference between the above two methods? Which one is preferred
over the other in what situations?

Requirements.txt is used to set up an  development environment.
It is used by the developers to prepare the development environment.

setup.py is used to create packages that can be redistributed .
It is used to install packages in the end user system.

5. Read about "site-packages". Find the difference between the contents of your
package in the site-packages directory and your development directory

site-packages is the target directory of manually built Python packages. When we build and install Python packages from source (probably by executing python setup.py install), the installed modules are found in site-packages by default

6. Figure out the difference between a whl file format and other file types for Python
package

A whl.file is a zip ready to install built distribution.wheels are smaller and faster to install.Installing a source distribution runs the setup.py wheels cut it down.

7. What is editable mode in a package installation?

`pip install -e <path/url> ` -e or --editable installs a package in editable or development mode .This enables users to edit a package as like project files.


## Mypy
1. Static vs Dynamic type checking 

    Static type checking is done without runing the program. 
    C, C++, Java are examples of statically typed languages.

    Dynamic type checking is done during the runtime.
    Python, Javascript, C# are examples of dynamically typed languages

2. What is a type checker ?

  A type checker checks whether the operands of an operator are of compatable types

3. Why we need one for Python ?

Type checking helps find bugs in a faster and easier way .Static typing makes programs easier to understand and maintain with the presence of type declarations

4. Write an example programs with static typing using mypy
Example program:
```
from numpy import arange, argmax

def addition(var_a:int,var_b:int) -> int:
    ans = a + b

    return ans


def subtraction(var_a:int, var_b:int) -> str:
    ans = a - b
    return ans



a = arange(5)
print(a)
print(argmax(a))
```
5. mypy.ini
  a. What are the contents of this file
  
  mypy.ini is the mypy configuration file. It contains section names in square brackets and flag settings of the form NAME = VALUE. 

  b. Create mypy.ini and add it to your repo

  mypy.ini can be found under code dir

## Pylint
1. What is Linting / Static Code analysis

Linting is the process of checking the code for basic stylistic mistakes. It doesn't verify whether the code works or not, it checks that the code looks as good as possible and is readable by others.
pylint is a tool for linting code.

2. Write an example program and run pylint over that file
Example program:
```
import sys
from numpy import arange, argmax

def addition(var_a, var_b):
    ans = var_a + var_b
    return ans

def subtraction(var_a,var_b):
    ans = var_a - var_b
    return ans

a = arange(5)
print(a)
print(argmax(a))
```

![](https://github.com/yashwanthika/Zoho-internship/blob/main/week_2/images/Pylint_example.png)

3. pylintrc file

  a. What are the contents of this file

  Pylintrc is a configuration which contains the coding and quality standards


  b. Create pylintrc file and add to your repo

  pylintrc can be found under code dir