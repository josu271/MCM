import unittest
from Calculo import lcm


class TestLCM(unittest.TestCase):
    def test_lcm(self):
        self.assertEqual(lcm(4, 5), 20)
        self.assertEqual(lcm(3, 7), 21)
        self.assertEqual(lcm(12, 15), 60)
        self.assertEqual(lcm(0, 5), 0)  # El MCM con 0 es 0
        self.assertEqual(lcm(5, 0), 0)

if __name__ == '__main__':
    unittest.main()
