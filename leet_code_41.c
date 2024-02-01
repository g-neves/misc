#include <stdio.h>

int firstMissingPositive(int* nums, int numsSize) {
    int i = 0;
    while (i < numsSize) {
        if (nums[i] > 0 && nums[i] <= numsSize && nums[nums[i] - 1] != nums[i]) {
            int tmp = nums[nums[i] - 1];
            nums[nums[i]-1] = nums[i];
            nums[i] = tmp;
            i--;
        }
        i++;
    }

    for (int i = 0; i < numsSize; i++) {
        if (nums[i] != i + 1) {
            return i + 1;
        }
    }

    return numsSize + 1;
}

void runTest(int* nums, int numsSize, int expected) {
    int result = firstMissingPositive(nums, numsSize);
    printf("Test Case: ");
    for (int i = 0; i < numsSize; i++) {
        printf("%d ", nums[i]);
    }
    printf("=> Expected: %d, Actual: %d\n", expected, result);
}

int main() {
    int nums1[] = {1, 2, 0};
    runTest(nums1, sizeof(nums1) / sizeof(nums1[0]), 3);

    int nums2[] = {3, 4, -1, 1};
    runTest(nums2, sizeof(nums2) / sizeof(nums2[0]), 2);

    int nums3[] = {7, 8, 9, 11, 12};
    runTest(nums3, sizeof(nums3) / sizeof(nums3[0]), 1);

    return 0;
}

