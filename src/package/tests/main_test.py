import unittest
import numpy as np
from src.package.main import sum

class TestSumFunction(unittest.TestCase):
    def test_sum_basic_arrays(self):
        arr1 = np.array([1, 2, 3])
        arr2 = np.array([4, 5, 6])
        result = sum(arr1, arr2)
        expected = 21
        self.assertEqual(result, expected)
    
    def test_sum_single_element(self):
        arr1 = np.array([5])
        arr2 = np.array([10])
        result = sum(arr1, arr2)
        expected = 15
        self.assertEqual(result, expected)
    
    def test_sum_zeros(self):
        arr1 = np.array([0, 0, 0])
        arr2 = np.array([1, 2, 3])
        result = sum(arr1, arr2)
        expected = 6
        self.assertEqual(result, expected)
    
    def test_sum_negative_numbers(self):
        arr1 = np.array([-1, -2, -3])
        arr2 = np.array([1, 2, 3])
        result = sum(arr1, arr2)
        expected = 0
        self.assertEqual(result, expected)
    
    def test_sum_same_arrays(self):
        arr1 = np.array([1, 2, 3, 4, 5])
        arr2 = np.array([10, 20, 30, 40, 50])
        result = sum(arr1, arr2)
        expected = 165
        self.assertEqual(result, expected)
