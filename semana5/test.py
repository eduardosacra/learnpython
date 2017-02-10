import unittest

def fatorial(x):
    if x == 0:
        return 1
    if x > 1:
        return x * fatorial(x-1)
    else:
        return x


class TestFatorial(unittest.TestCase):
    """docstring for ."""
    def test_fatorial2(self):
        self.assertEqual(fatorial(2),2)
    def test_fatorial5(self):
        self.assertEqual(fatorial(5),120)
    def test_fatorial0(self):
        self.assertEqual(fatorial(0),1)

if __name__ == '__main__':
    unittest.main()
