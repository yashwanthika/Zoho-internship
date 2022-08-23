# Pip
Create a Pypi compatible package for some toy Python code of yours
Installation:
```
pip install -i https://test.pypi.org/simple/ additiveiter==1.0.1
```
Usage:
```
from additiveiter import add_iter

add_iter([9,5,3,2,1])
```
returns 15
# Pytest
1. What is a unitest

The code is split into smallest testing parts called units and tested individually .This process is called as unit testing.

2. Write few unit tests and run pytest
Let the functionality to be tested be sum of iterative elements
```
def add_iter(args):
    result=0
    for item in args:
        result=result+item
    return result
```
Test on tuple:
```
import pytest

import src.additiveiter.add_iter as add

def test_tuple(input_data):
        
   assert add.add_iter(tuple(input_data))== 17
```
Test on set:
```
import pytest

import src.additiveiter.add_iter as add

def test_set(input_data):
        
   assert add.add_iter(set(input_data))== 15
```
3. Get the report of those runs
To save the runs as report
```
$ pytest --html=pytest_report.html
```
![pytest_report](https://github.com/yashwanthika/Zoho-internship/blob/main/week_2/images/pytest_report.png)

a. Save the report
Test report gets saved to pytest_report.html

4. Write sample pytest fixtures
a. Reuse them inside uni tests
```
import pytest

@pytest.fixture
def input_data():
   data = [1,2,3,4,5]
   return data

```
b. Reuse them inside other fixtures
```
import pytest

@pytest.fixture
def input_data_small():
   data = [1,2,3,4,5]
   return data


@pytest.fixture
def input_data(input_data_small):
   input_data_small.append(2)
   return input_data_small
```
5. Use temporary directories and files
```
import pytest

import src.additiveiter.add_iter as add


def test_create_file(tmp_path,input_data):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello.txt"
    p.write_text(str(input_data))
    assert p.read_text() == str(input_data)
```
6. What is conftest.py

conftest.py  is used to store test configurataions and fixtures used by other test functions
a. Create a sample file
```
import pytest

@pytest.fixture
def input_data_small():
   data = [1,2,3,4,5]
   return data


@pytest.fixture
def input_data(input_data_small):
   input_data_small.append(2)
   return input_data_small
```

7. Mock objects
```
import pytest

import src.additiveiter.add_iter 

def addition():
    return src.additiveiter.add_iter([1,2,3,4])

def test_mocking_function(mocker):
    mocker.patch("src.additiveiter.add_iter", return_value=2)
    assert addition() == 2, "Value should be mocked"
```

8. Catch raised Exceptions
```
import pytest

import src.additiveiter.add_iter as add

def test_list(input_data):
    try:
        sum=add.add_iter(input_data)
    except Exception as exc:
        assert False, f"'test_list' raised an exception {exc}"

    assert sum == 17
```

To run tests
```
$ pytest .
```
![pytest_example](https://github.com/yashwanthika/Zoho-internship/blob/main/week_2/images/pytest_example.png)
