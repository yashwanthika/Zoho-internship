import pytest

import src.additiveiter.add_iter as add

def test_set(input_data):
        
   assert add.add_iter(set(input_data))== 15