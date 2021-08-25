import pytest
from analyser.plotting import *

def test_summ():
    assert summ(2,3) == 5

def test_given_x_y_unequal_throw_exception():
    with pytest.raises(Exception) as err:
        x = [0, 1, 2, 3, 4, 5]
        y = [0, 1, 2, 3]
        scatter(x, y)
