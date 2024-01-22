#!/usr/bin/env python3

from typing import List
import unittest


def solve(nums: List[int], k: int) -> int:
    if len(nums) == 1:
        return nums[0] if k % 2 == 0 else -1
    try:
        return max(max(nums[:k-1]), nums[k]) if nums[:k-1] and k else nums[k]
    except IndexError:
        return max(nums[:k-1]) if nums[:k-1] else -1

class TestMaximizeTopMostElement(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(solve([], 3), -1)

    def test_empty_list_k_equals_0(self):
        self.assertEqual(solve([], 0), -1)

    def test_single_list_k_even(self):
        self.assertEqual(solve([1], 2), 1)
        
    def test_single_list_k_odd(self):
        self.assertEqual(solve([1], 3), -1)

    def test_k_equals_0(self):
        self.assertEqual(solve([1,2,3], 0), 1)
        
    def test_len_nums_equals_k(self):
        self.assertEqual(solve([1,2,3], 3), 2)

    def test_big_k(self):
        self.assertEqual(solve([99,95,68,24,18], 69), 99)

if __name__ == "__main__":
    unittest.main()
