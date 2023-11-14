import unittest
from src.query_generator import QueryGenerator

class TestCoreFunctionality(unittest.TestCase):
    def test_sample(self):
        self.assertEqual('sample test case', 'Sample Test Case'.lower())
    
    