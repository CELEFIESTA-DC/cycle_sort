#!/usr/bin/python3
"""





#####################################################################
    

                        DO NOT EDIT THIS FILE


#####################################################################






"""

import unittest
from main import cycle_sort 

class Tests(unittest.TestCase):
    def test(self):
        self.assertEqual(cycle_sort([5,3,1,2,3,0,-100,-9]),[-100, -9, 0, 1, 2, 3, 3, 5])
        

if __name__=='__main__':
    unittest.main()

    
