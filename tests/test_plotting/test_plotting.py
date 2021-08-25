import pytest
from os.path import exists
from analyser.plotting import *

def test_given_x_y_unequal_throw_exception():
    with pytest.raises(Exception) as err:
        x = [0, 1, 2, 3, 4, 5]
        y = [0, 1, 2, 3]
        scatter_plot(x, y)

def test_given_x_y_z_unequal_throw_exception():
    with pytest.raises(AssertionError) as err:
        x = [0, 1, 2, 3, 4, 5]
        z = [1, 2]
        scatter_plot(x, x, z=z)


