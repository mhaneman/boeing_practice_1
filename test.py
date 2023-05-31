import unittest
from main import MyStack


class TestStringMethods(unittest.TestCase):

    def test_positive(self):
        s = MyStack()
        s.push(0)
        s.push(1)
        s.push(2)
        self.assertEqual(s.peak(), 2)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)
        self.assertEqual(s.pop(), 0)

    def test_negative(self):
        s = MyStack()
        with self.assertRaises(ValueError):
            s.pop()


if __name__ == '__main__':
    unittest.main()
