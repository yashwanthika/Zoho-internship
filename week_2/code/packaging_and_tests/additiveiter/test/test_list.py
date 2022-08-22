import pytest

import src.additiveiter.add_iter as add

def test_list(input_data):
    try:
        sum=add.add_iter(input_data)
    except Exception as exc:
        assert False, f"'test_list' raised an exception {exc}"

    assert sum == 17