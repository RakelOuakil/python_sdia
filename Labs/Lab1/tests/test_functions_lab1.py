from pathlib import Path
import sys


LAB_DIR = Path(__file__).resolve().parent .parent
sys.path.insert(0, str(LAB_DIR))


from ipynb.fs.defs.lab1 import is_unique, triangle_shape


def test_is_unique():
    assert is_unique([])
    assert is_unique([1])
    assert is_unique([1, 2, 3, 4])

    assert not is_unique([2, 3, 2])

def test_triangle_shape():
    assert triangle_shape(0) == ""
    assert triangle_shape(1) == "x"
    assert triangle_shape(2) == " x \nxxx"
    assert "\nxxxxxxxxxxx" in triangle_shape(6)



