import pytest

@pytest.fixture
def input_data_small():
   data = [1,2,3,4,5]
   return data


@pytest.fixture
def input_data(input_data_small):
   input_data_small.append(2)
   return input_data_small