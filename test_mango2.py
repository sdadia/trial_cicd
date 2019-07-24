import unittest
from mango2 import toga

class TestMango2(unittest.TestCase):
	def test_toga(self):
		self.assertEqual(3, toga(1,2))
		self.assertEqual(0, toga(0,0))
		self.assertEqual(-1, toga(0,-1))


if __name__ == '__main__':
    unittest.main()