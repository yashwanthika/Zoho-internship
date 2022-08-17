# Week 2
# Day 1 : 16 Aug 2022

## Virtualenv:
A virtual environment is a Python environment such that the Python interpreter, libraries and scripts installed into it are isolated from those installed in other virtual environments, and  libraries installed in the system Python (base).
To install virtualenv:
```
$ pip install virtualenv
```
To create a virtual environment:
```
$ python<version> -m venv <virtual-environment-name>
```
To activate virtual environment
```
$ source env/bin/activate
```
To deactivate a virtual environment
```
$ deactivate
```

## Pip
Pip is a dependency management tool that comes together with the standard Python installation for Windows and can be installed via Homebrew for MacOS and the distribution app manager for Linux systems.
To install pip
```
$ pip install [package_name]
```

Command to list the packages installed through pip.
```
$ pip list
```
To uninstall packages
```
$ pip uninstall [package_name]
```
## Conda

Conda is a dependency management tool that comes with Anaconda.

To install packages through conda
```
$ conda install [packagename]
```
Command to list the packages installed through conda
```
$ conda list
```
To uninstall packages
```
$ conda remove [packagename]
```

## Poetry

poetry is a tool to handle dependency installation as well as building and packaging of Python packages.It helps us to declare, manage and install dependencies of Python projects.

To install poetry either use 
```
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```
or 

```
$ pip install poetry
```
To check the version of poetry 
```
$ poetry --version
```
To edit poetry config settings and repositories.
```
$ poetry config --list
```
```
$ poetry config virtualenvs.in-project true
```

To create a pyproject.toml file and provide basic information about your package
```
$ poetry init
```
The add command adds required packages to your pyproject.toml and installs them.
```
$ poetry add django
```
The install command reads the pyproject.toml file from the current project, resolves the dependencies, and installs them.
```
$ poetry install
```
When Poetry has finished installing, it writes all of the packages and the exact versions of them that it downloaded to the poetry.lock file, locking the project to those specific versions

To list all of the available packages:
```
$ poetry show
```
The run command executes the given code inside the project’s virtualenv .
we can either rum 
```
$ poetry run python [filename].py
```
or
```
$ poetry shell
$ python [filename].py
```
The build command builds the source and wheels archives
```
$ poetry build
```
The publish command publishes the package, previously built with the build command, to the remote repository.
```
$ poetry publish
```

when compared to pip and conda poetry provides better handling of dependency conflicts.

## Mypy

to install mypy
```
$ pip install mypy
```

```
$ mypy [filename].py
```

## Pylint

Pylint is a tool for linting code. Linting is the process of checking the code for basic stylistic mistakes. It doesn't verify whether the code works or not, it checks that the code looks as good as possible and is readable by others.


To install pylint
```
$ pip install pylint
```
To check version (to verify pylint installation)
```
$ pylint --version
```
To run pylint over the code
```
$ pylint filename.py
```


## Black
Black is a code reformatting tool .It reformats the code to improve readability.

To install black
```
$ pip install black
```
To check if there is any code to reformat
```
$ black --check --target-version=py35 .
```
To reformat code
```
$ black --target-version=py35 .
```

## Parallel processing:

Parallel processing can be done using multi processing and joblib

Multiprocessing
```
from multiprocessing import Pool
import time
import plotly.express as px
import plotly
import pandas as pd

def f(x):
    return x**2

def runner(list_length):
    print(f"Size of List:{list_length}")
    t0 = time.time()
    result1 = [f(x) for x in list(range(list_length))]
    t1 = time.time()
    print(f"Without multiprocessing we ran the function in {t1 - t0:0.4f} seconds")
    time_without_multiprocessing = t1-t0
    t0 = time.time()
    pool = Pool(8)
    result2 = pool.map(f,list(range(list_length)))
    pool.close()
    t1 = time.time()
    print(f"With multiprocessing we ran the function in {t1 - t0:0.4f} seconds")
    time_with_multiprocessing = t1-t0
    return time_without_multiprocessing, time_with_multiprocessing

if __name__ ==  '__main__':
    times_taken = []
    for i in range(1,9):
        list_length = 10**i
        time_without_multiprocessing, time_with_multiprocessing = runner(list_length)
        times_taken.append([list_length, 'No Mutiproc', time_without_multiprocessing])
        times_taken.append([list_length, 'Multiproc', time_with_multiprocessing])

    timedf = pd.DataFrame(times_taken,columns = ['list_length', 'type','time_taken'])
    fig =  px.line(timedf,x = 'list_length',y='time_taken',color='type',log_x=True)
    plotly.offline.plot(fig, filename='comparison_bw_multiproc.html')
    
```
![output](https://github.com/yashwanthika/Zoho-internship/blob/main/week_2/images/multiprocessing_example.png)

Joblib

```
from multiprocessing import Pool
import time
import plotly.express as px
import plotly
import pandas as pd
from joblib import Parallel, delayed

def f(x):
    time.sleep(2)
    return x**2


def runner(list_length):
    print(f"Size of List:{list_length}")
    t0 = time.time()
    result1 = Parallel(n_jobs=8)(delayed(f)(i) for i in range(list_length))
    t1 = time.time()
    print(f"With joblib we ran the function in {t1 - t0:0.4f} seconds")
    time_without_multiprocessing = t1-t0
    t0 = time.time()
    pool = Pool(8)
    result2 = pool.map(f,list(range(list_length)))
    pool.close()
    t1 = time.time()
    print(f"With multiprocessing we ran the function in {t1 - t0:0.4f} seconds")
    time_with_multiprocessing = t1-t0
    return time_without_multiprocessing, time_with_multiprocessing

if __name__ ==  '__main__':
    times_taken = []
    for i in range(1,16):
        list_length = i
        time_without_multiprocessing, time_with_multiprocessing = runner(list_length)
        times_taken.append([list_length, 'No Mutiproc', time_without_multiprocessing])
        times_taken.append([list_length, 'Multiproc', time_with_multiprocessing])

    timedf = pd.DataFrame(times_taken,columns = ['list_length', 'type','time_taken'])
    fig =  px.line(timedf,x = 'list_length',y='time_taken',color='type')
    plotly.offline.plot(fig, filename='comparison_bw_multiproc.html')
 ```
![output](https://github.com/yashwanthika/Zoho-internship/blob/main/week_2/images/joblib_example.png)
