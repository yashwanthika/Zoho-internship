# Week 2
# Day:3 18 AUG 2022

## Pip
1. What is a package manager / installer

  Package managers are tools for software developers to help them easily share and install software libraries and also for managing dependencies.
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
