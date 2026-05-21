import unittest
from utils import clean_string_data

class TestCoreFunctions(unittest.TestCase):
    def test_sanitization(self):
        self.assertEqual(clean_string_data('  DATA '), 'data')

if __name__ == '__main__':
    unittest.main()