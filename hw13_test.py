# TODO get 100% test coverage for hw13.py

'''
    This file will test all code in hw13.py
    
    
'''

import unittest
from hw13 import my_func
import hw13

KEY_INPUT = "input"
KEY_EXPECTED = "expected"
KEY_ITERATIONS = 0
KEY_INITIAL = 0
KEY_SECOND = 0

class testHW13(unittest.TestCase):
    def setUp(self):
        self.success_test_params = [
            {
                KEY_INPUT: {
                    KEY_ITERATIONS: 0,
                    KEY_INITIAL : 0,
                    KEY_SECOND : 0
                },
                KEY_EXPECTED : "Don't iterate"
            },
            {
                KEY_INPUT: {
                    KEY_ITERATIONS: 2,
                    KEY_INITIAL : 1,
                    KEY_SECOND : 9
                },
                KEY_EXPECTED : "counter is 10"
            },
            {
                KEY_INPUT: {
                    KEY_ITERATIONS: 2,
                    KEY_INITIAL : 1,
                    KEY_SECOND : -10
                },
                KEY_EXPECTED : "initial is -10"
            },
            
            
        ]
        
        
    def test_hw13_success(self):
        for test in self.success_test_params:
            response = hw13.my_func(test[KEY_INPUT][KEY_ITERATIONS],
                                    test[KEY_INPUT][KEY_INITIAL],
                                    test[KEY_INPUT][KEY_SECOND])
            expected = test[KEY_EXPECTED]
            self.assertEqual(response,expected)
            
if __name__ == '__main__':
    unittest.main()