import pytest

import src.additiveiter.add_iter 

def addition():
    return src.additiveiter.add_iter([1,2,3,4])

def test_mocking_function(mocker):
    mocker.patch("src.additiveiter.add_iter", return_value=2)
    assert addition() == 2, "Value should be mocked"