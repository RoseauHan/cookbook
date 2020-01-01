---
title: valid_palindrome
tags: two pointer, easy
authors:
  - roseau
date: 2020-01-01
---
## Addr
https://leetcode.com/problems/valid-palindrome/description/

## Desc
```
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
```

## Algo
这是一道考察回文的题目，而且是最简单的形式，即判断一个字符串是否是回文。

针对这个问题，我们可以使用头尾双指针:

- 如果两个指针的元素不相同，则直接返回false,
- 如果两个指针的元素相同，我们同时更新头尾指针，循环。 直到头尾指针相遇。

时间复杂度为O(n).

## Code
```python3
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                break
        return right <= left

    def isPalindrome2(self, s: str) -> bool:
        """
        使用语言特性进行求解
        """
        s = ''.join(i for i in s if i.isalnum()).lower()
        return s == s[::-1]
```