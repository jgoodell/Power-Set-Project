import unittest
from power_set import power_set

class PowerSetTestCase(unittest.TestCase):
    def setUp(self):
        self.test_set01 = []
        self.test_set02 = [1,2,3]
        self.test_set03 = ["a","d","u"]
        self.test_set04 = [1,"h",{}]
        self.test_set05 = [None,{}]

    def tearDown(self):
        pass

    def test_set01(self):
        self.assertEqual(power_set(self.test_set01),[[]])

    def test_set02(self):
        self.assertEqual(power_set(self.test_set02).sort(),[[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]].sort())

    def test_set03(self):
        self.assertEqual(power_set(self.test_set03).sort(),[[],["a"],["b"],["c"],["a","b"],["a","c"],["b","c"],["a","b","c"]].sort())

    def test_set04(self):
        power_set(self.test_set04)
        self.assertEqual(power_set(self.test_set04).sort(),[[],[1],["h"],[{}],[1,"h"],[1,{}],["h",{}],[1,"h",{}]].sort())
        
