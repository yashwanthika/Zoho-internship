import pytest

import src.additiveiter.add_iter as add

def test_tuple(input_data):
        
   assert add.add_iter(tuple(input_data))== 17