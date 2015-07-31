#Imports unittest module
import unittest
from layer_map_merge import *

class TestLayerMapMerge(unittest.TestCase):
    def testgolden(self):
        layer_map_merge(["input1.txt","input2.txt","input3.txt","input4.txt","input5.txt"])
        self.assertTrue(filecmp.cmp("golden.txt","output.txt"))

if __name__ == '__main__':
    unittest.main()
