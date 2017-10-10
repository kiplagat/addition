import unittest
from addition import addition
class testsum(unittest.TestCase):
     def test_number_is_Not_a_string(self):
	     self.assertRaises(TypeError)
     def test_answer_is_correct(self):
	     self.assertEqual(addition(2,3),5)
     def test_solution_is_not_product(self):
	     self.assertRaises(TypeError,addition(2,3),6)
if __name__ == "__main__":
 unittest.main()
