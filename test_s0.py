import unittest
from main import s1

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(s1(1,1),1/9 )

