from typing import List, Tuple
import unittest



def find_max_subarray(arr: List[int]) -> int:
    if not arr:
        return 0

    left = 0
    right = len(arr) - 1

    ret_val = find_max_subarray_recursor(arr, left, right)
    if ret_val < 0:
        return 0

    return ret_val

def find_cross_max(arr: List[int], left: int, right: int, mid: int) -> int:
    # Left sum
    left_sum = 0
    curr_sum = 0
    for i in range(mid-1, left-1, -1):
        curr_sum += arr[i]
        left_sum = max(curr_sum, left_sum)

    # Right sum
    right_sum = 0
    curr_sum = 0
    for i in range(mid, right+1):
        curr_sum += arr[i]
        right_sum = max(curr_sum, right_sum)

    return left_sum + right_sum

def find_max_subarray_recursor(arr: List[int], left: int, right: int) -> int:
    # Base case
    if left == right:
        return arr[left]

    # Pre-processing
    mid = (left + right) // 2

    # Recursion
    left_max = find_max_subarray_recursor(arr, left, mid)
    right_max = find_max_subarray_recursor(arr, mid+1, right)
    cross_max = find_cross_max(arr, left, right, mid)

    # Pos-processing
    return max(left_max, right_max, cross_max)

class TestMaxSubarray(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(find_max_subarray([]), 0)

    def test_all_negative_numbers(self):
        self.assertEqual(find_max_subarray([-2, -5, -7, -1, -3]), 0)

    def test_single_positive_number(self):
        self.assertEqual(find_max_subarray([5]), 5)

    def test_simple_case(self):
        self.assertEqual(find_max_subarray([1, -2, 3, -4, 5]), 5)

    def test_all_positive_numbers(self):
        self.assertEqual(find_max_subarray([1, 2, 3, 4, 5]), 15)

    def test_mixed_positive_and_negative_numbers(self):
        self.assertEqual(find_max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)


def main():
    unittest.main()

if __name__ == "__main__":
    main()

