import unittest

def multiply(x,y):
    return x * y


class TestMultiply(unittest.TestCase):

    def text_multiply(self):
        text_x = 5
        text_y = 10
        self.assertEqual(multiply(text_x, text_y), 50, "Should be 50")

if __name__ == "__main__":
    unittest.main()

