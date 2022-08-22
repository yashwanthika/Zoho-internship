import pytest

import src.additiveiter.add_iter as add


def test_create_file(tmp_path,input_data):
    d = tmp_path / "sub"
    d.mkdir()
    p = d / "hello.txt"
    p.write_text(str(input_data))
    assert p.read_text() == str(input_data)