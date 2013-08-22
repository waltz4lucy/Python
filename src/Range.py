import unittest
from collections import defaultdict
import sys

class RangeData:
    def __init__(self):
        self.data = defaultdict(list)

    def range(self, start=0, length=None):
        if length == None:
            stop = sys.maxint
        else:
            stop = start + length
        return list([key] + self.data[key]
                    for key in sorted(self.data)
                    if start <= key < stop)

    def insert(self, start, length, char):
        for i in range(start, start + length):
            self.data[i] += char
        return ' ' * start + char * length

a,b,c = 'abc'
class TestRange(unittest.TestCase):
    def test_range_data(self):
        rd = RangeData()
        self.assertEqual(rd.range(), [])

        self.assertEqual(rd.insert(3, 2, a), '   aa')
        self.assertEqual(rd.insert(4, 3, b), '    bbb')
        self.assertEqual(rd.range(), [
            [3, a],
            [4, a, b],
            [5, b],
            [6, b]
        ])
        self.assertEqual(rd.range(3, 3), [
            [3, a],
            [4, a, b],
            [5, b],
        ])

        self.assertEqual(rd.insert(1, 4, c), ' cccc')
        self.assertEqual(rd.range(), [
            [1, c],
            [2, c],
            [3, a, c],
            [4, a, b, c],
            [5, b],
            [6, b]
        ])


if __name__ == '__main__':
    unittest.main()