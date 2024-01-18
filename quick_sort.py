#!/usr/bin/env python3

from typing import List
import unittest

def qs(arr: List[int], low: int, high: int) -> None:
    # Base cases
    if low >= high:
        return

    # Pre recursion
    pivot_idx = partition(arr, low, high)

    # Recursion
    qs(arr, low, pivot_idx-1)
    qs(arr, pivot_idx+1, high)

def partition(arr: List[int], low: int, high: int) -> int:
    pivot = arr[high]

    idx = low
    for i in range(low, high):
        if arr[i] <= pivot:
            tmp = arr[i]
            arr[i] = arr[idx]
            arr[idx] = tmp
            idx += 1

    arr[high] = arr[idx]
    arr[idx] = pivot

    return idx

def quick_sort(arr: List[int]) -> None:
    low = 0
    high = len(arr) - 1
    qs(arr, low, high)

class Testquick_sort(unittest.TestCase):
    
    def test_empty_list(self):
        data = []
        quick_sort(data)
        self.assertEqual(data, [])

    def test_sorted_list(self):
        data = [1, 2, 3, 4, 5]
        quick_sort(data)
        self.assertEqual(data, [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        data = [5, 4, 3, 2, 1]
        quick_sort(data)
        self.assertEqual(data, [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        quick_sort(data)
        self.assertEqual(data, [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])


if __name__ == '__main__':
    unittest.main()
