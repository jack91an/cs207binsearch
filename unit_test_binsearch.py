
from pytest import raises
import numpy as np
import unittest as ut


from ~/cs207binsearch/binsearch.py import binary_search

class MyTest(unittest.TestCase):
    
    def test_original(self):
        input = list(range(5))
        self.assertEqual(binary_serach(input,5), 5)

    def test_nan(self):
        input = [np.nan]
        with self.assertRaises(TypeError):
            binary_search(input,2)
            
    def test_numeric(self):
        input=['a', 'b', 7, 10]
        with self.assertRaises(TypeError):
            binary_search(input,3)
            
    def test_empty(self):
        self.assertEqual(binary_search([],1),-1)
        
    def test_one_element(self):
        self.assertEqual(ut.binary_search([1],1),-1)
    
    def test_two_element(self):
        self.assertEqual(binary_search([1,2],1),-1)
    
    def test_boundary(self):
        input = list(range(5))
        self.assertEqual(binary_search(input,1,3,1),-1)
        
    def test_needle_out_of_range(self):
        input = list(range(5))
        self.assertEqual(binary_search(input,11),-1)
        self.assertEqual(binary_search(input,-1),-1)
        
    def test_extremes(self):
        input = list(range(5))
        self.assertEqual(binary_search(input,9),9)
        self.assertEqual(binary_search(input,0),0)
        
    def test_multiple(self):
        input = [3]*10
        self.assertEqual(binary_search(input,3),0)
        
    def test_overflow(self):
        input = list(range(5))
        self.assertEqual(binary_search(input,np.inf+1),-1)
            
if __name__ == '__main__':
    unittest.main()