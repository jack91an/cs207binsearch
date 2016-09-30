
import numpy as np

from binsearch import binary_search

def test_original():
    input = list(range(5))
    self.assertEqual(binary_serach(input,5), 5)

def test_nan():
    input = [np.nan]
    with self.assertRaises(TypeError):
        binary_search(input,2)

def test_numeric():
    input=['a', 'b', 7, 10]
    with self.assertRaises(TypeError):
        binary_search(input,3)

def test_empty():
    self.assertEqual(binary_search([],1),-1)

def test_one_element():
    self.assertEqual(ut.binary_search([1],1),-1)

def test_two_element():
    self.assertEqual(binary_search([1,2],1),-1)

def test_boundary():
    input = list(range(5))
    self.assertEqual(binary_search(input,1,3,1),-1)

def test_needle_out_of_range():
    input = list(range(5))
    self.assertEqual(binary_search(input,11),-1)
    self.assertEqual(binary_search(input,-1),-1)

def test_extremes():
    input = list(range(5))
    self.assertEqual(binary_search(input,9),9)
    self.assertEqual(binary_search(input,0),0)

def test_multiple():
    input = [3]*10
    self.assertEqual(binary_search(input,3),0)

def test_overflow():
    input = list(range(5))
    self.assertEqual(binary_search(input,np.inf+1),-1)
            