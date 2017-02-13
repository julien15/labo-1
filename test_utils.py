# test_utils.py
# Author: Sébastien Combéfis
# Version: February 2, 2016

import unittest
import utils
import program

class TestUtils(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(program.fact(5),120)
        
    
    def test_roots(self):
        # À compléter...
        pass
    
    def test_integrate(self):
        # À compléter...
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
