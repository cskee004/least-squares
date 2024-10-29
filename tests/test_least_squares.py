import numpy as np

from tests.least_squares import *

test_file = "./data/test-input-no-labels.txt"
time_step = 30
temperature_table = build_table(test_file, time_step)

def test_build_y_matrix():
    y_matrix = build_y_matrix(temperature_table, 0)
    expected_y_matrix = np.array([61.0, 80.0, 62.0, 83.0, 68])
    assert np.array_equal(y_matrix, expected_y_matrix)
    
def test_build_x_matrix():
    x_matrix = build_x_matrix(temperature_table)
    expected_x_matrix = np.array([[1, 0],
                                  [1, 30],
                                  [1, 60],
                                  [1, 90],
                                  [1, 120]])
    np.testing.assert_array_equal(x_matrix, expected_x_matrix)
    
def test_transpose():
    x_matrix = build_x_matrix(temperature_table)
    xT = transpose_matrix(x_matrix)
    expected_xT_matrix = np.array([ [1, 1, 1, 1, 1,],
                                    [0, 30, 60, 90, 120]])
    np.testing.assert_array_equal(xT, expected_xT_matrix)
