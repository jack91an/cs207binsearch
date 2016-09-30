
import numpy as np

from binsearch import binary_search

def test_original():
    input = list(range(5))
    assert binary_serach(input, 2) == 2

def test_nan():
    input = [np.nan]
    with raises(TypeError):
        binary_search(input, np.nan)

def test_numeric():
    input=['a', 'b', 7, 10]
    with raises(TypeError):
        binary_search(input,'a')

def test_empty():
    with raises(ValueError):
        binary_search([],1)

def test_one_element():
    assert binary_search([1],1) == 0

def test_two_element():
    assert binary_search([1,2],1) == 0

def test_boundary():
    input = list(range(5))
    assert binary_search(input,1,3,1) == -1

def test_needle_out_of_range():
    input = list(range(5))
    assert binary_search(input,6) == -1
    assert binary_search(input,-1) == -1

def test_extremes():
    input = list(range(5))
    assert binary_search(input,4) == 4
    assert binary_search(input,0) == 0

def test_multiple():
    input = [3]*10
    assert binary_search(input,3) == 0

def test_overflow():
    input = list(range(5))
    assert binary_search(input,np.inf+1) == -1
            