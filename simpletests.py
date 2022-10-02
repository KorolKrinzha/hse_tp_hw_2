import unittest
# Using unittest because it is a standard library for testing
from NumbersOperator import NumbersOperator


class SimpleTests(unittest.TestCase):
    # We need to go through several tests:
    # 1. when given low amount of correct numbers
    # 2. when given input with incorrect variable types (str, float, etc)
    # 3. all of these tests must be carried out for all four operations 
    
    # Tests for sum
    # check usual list of characters
    def test_sum_regular(self):
        test_object_1 = NumbersOperator('test_1.txt')

        self.assertEqual(test_object_1.sum(), 28, f'Test is correct. Amount of numbers: {test_object_1.getNumberListSize()}')
    
    # Check when given wrong type 
    def test_sum_type(self):
        test_object_2 = NumbersOperator('test_2.txt')
        with self.assertRaises(TypeError):
            test_object_2.sum()
        
    def test_max_regular(self):
        test_object_1 = NumbersOperator('test_1.txt')
        self.assertEqual(test_object_1.max(), 7, f'Test is correct. Amount of numbers: {test_object_1.getNumberListSize()}')

if __name__ == '__main__':
    unittest.main()