---
title: Remove_Duplicates_from_Sorted_Array
tags: array, two pointer
authors:
  - roseau
date: 2020-01-01
---

## Addr

https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

## Desc

```

Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.

```

## Algo

Since the array is already sorted, we can keep two **pointers** i and j, where i is the slow-runner while j is the fast-runner. As long as nums[i] = nums[j], we increment j to skip the duplicate.

When we encounter nums[j] != nums[i], the duplicate run has ended so we must copy its value to nums[i + 1]. i is then incremented and we repeat the same process again until j reaches the end of array.

![图片https://github.com/MisterBooo/LeetCodeAnimation](https://github.com/azl397985856/leetcode/raw/master/assets/26.remove-duplicates-from-sorted-array.gif)

## Code

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums:
            slow = 0
            for fast in range(1, len(nums)):
                if nums[fast] != nums[slow]:
                    slow += 1
                    nums[slow] = nums[fast]
            return slow + 1
        else:
            return 0
```
