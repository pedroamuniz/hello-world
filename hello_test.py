import unittest
import hello

class greeting_test(unittest.TestCase):
    def test_pedro(self):
        self.assertEqual(hello.hello('Pedro') , 'Hello Pedro')


if __name__ == "__main__":
    unittest.main()