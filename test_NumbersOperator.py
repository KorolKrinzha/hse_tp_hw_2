import unittest
# Using unittest because it is a standard library for testing
from NumbersOperator import NumbersOperator


class SimpleTests(unittest.TestCase):
    # We need to go through several tests:
    # 1. when given low amount of correct numbers (complete for all four operations)
    # 2. when given input with incorrect variable types (str, float, etc)
    # 3. when given input with incorrect filename (for example, file doesnt exist)
    # 4. when given a great amount of correct numbers (complete for all four operations)
    
    # At first, we need to check how we handle mistakes
    # Mistakes (wrong filename, wrong type) occur to all four operations same way 
    # That is why we are going to create these tests for only one method
    # We will take sum() as an example. However, it can be any other method
    
    
    # Check when given wrong type 
    def test_type(self):
        test_object_2 = NumbersOperator('tests_txt/test_2.txt')
        with self.assertRaises(TypeError):
            test_object_2.sum()
    
    # Check when given wrong filename
    def test_filename(self):
        test_object_3 = NumbersOperator('tests_txt/test_unknown.txt')
        with self.assertRaises(TypeError):
            test_object_3.sum()
    
    
    # We have set tests for handling errors. Now we need to go through each operation
    
    # Tests for max
    # check usual list of numbers
    def test_max_regular(self):
        test_object_1 = NumbersOperator('tests_txt/test_1.txt')
        self.assertEqual(test_object_1.max(), 7, f'Test is passed. Amount of numbers: {test_object_1.getNumberListSize()}')
        
    # check big list of numbers
    def test_max_big(self):
        test_object_2 = NumbersOperator('tests_txt/test_3.txt')
        self.assertEqual(test_object_2.max(), 19997, f'Test is passed. Amount of numbers: {test_object_2.getNumberListSize()}')
    
    # Tests for min
    # Check usual list of numbers
    def test_min_regular(self):
        test_object_1 = NumbersOperator('tests_txt/test_1.txt')
        self.assertEqual(test_object_1.min(),1, f'Test is passed. Amount of numbers: {test_object_1.getNumberListSize()}')
    
    # check big list of numbers
    def test_min_big(self):
        test_object_2 = NumbersOperator('tests_txt/test_3.txt')
        self.assertEqual(test_object_2.min(), 0, f'Test is passed. Amount of numbers: {test_object_2.getNumberListSize()}')

    # Tests for sum
    # check usual list of numbers
    def test_sum_regular(self):
        test_object_1 = NumbersOperator('tests_txt/test_1.txt')
        self.assertEqual(test_object_1.sum(), 28, f'Test is passed. Amount of numbers: {test_object_1.getNumberListSize()}')
    
    # check big list of numbers
    def test_sum_big(self):
        test_object_2 = NumbersOperator('tests_txt/test_3.txt')
        self.assertEqual(test_object_2.sum(), 99635288, f'Test is passed. Amount of numbers: {test_object_2.getNumberListSize()}')

                 
    # Tests for mult
    # check usual list of numbers
    def test_mult_regular(self):
        test_object_1 = NumbersOperator('tests_txt/test_1.txt')
        self.assertEqual(test_object_1.mult(), 5040, f'Test is passed. Amount of numbers: {test_object_1.getNumberListSize()}')
    
    # check big list of numbers
    def test_mult_big(self):
        test_object_2 = NumbersOperator('tests_txt/test_3.txt')
        self.assertEqual(test_object_2.mult(), 0, f'Test is passed. Amount of numbers: {test_object_2.getNumberListSize()}')

        
        

if __name__ == '__main__':
    unittest.main()