import os
import unittest

from app.main.service import math_service

numbers = [-1,2,3,4]

numbers2 = [1,-1,2,-2]

summingNumbers = [1,2,3,4,5]

class MathServiceTests(unittest.TestCase):
    def test_closest_to_zero(self):
        self.assertTrue(math_service.closestToZero(numbers) == -1)
        self.assertTrue(math_service.closestToZero(numbers2) == 1)

    def test_sum_of_numbers_while_loop(self):
        self.assertTrue(math_service.sumOfNumbersWhileLoop(summingNumbers) == 15)
        self.assertTrue(math_service.sumOfNumbersWhileLoop(numbers) == 8)
        self.assertTrue(math_service.sumOfNumbersWhileLoop(numbers2) == 0)
       
    def test_sum_of_numbers_for_loop(self):
        self.assertTrue(math_service.sumOfNumbersForLoop(summingNumbers) == 15)
        self.assertTrue(math_service.sumOfNumbersForLoop(numbers) == 8)
        self.assertTrue(math_service.sumOfNumbersForLoop(numbers2) == 0)

    def test_sum_of_numbers_recursion(self):
        self.assertTrue(math_service.sumOfNumbersRecursion(summingNumbers) == 15)
        self.assertTrue(math_service.sumOfNumbersRecursion(numbers) == 8)
        self.assertTrue(math_service.sumOfNumbersRecursion(numbers2) == 0)


if __name__ == '__main__':
   unittest.main()