---
title: valid_parentheses
tags: stack, easy
authors:
  - roseau
date: 2020-01-01
---


[valid_parentheses](https://leetcode.com/problems/valid-parentheses/description)

!!! question "valid_parentheses"

    Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Note that an empty string is also considered valid.

    ```
    Example 1:

    Input: "()"
    Output: true
    Example 2:

    Input: "()[]{}"
    Output: true
    Example 3:

    Input: "(]"
    Output: false
    Example 4:

    Input: "([)]"
    Output: false
    Example 5:

    Input: "{[]}"
    Output: true
    ```


??? tip

    Stack.

    ![图片来自：https://github.com/MisterBooo/LeetCodeAnimation](https://raw.githubusercontent.com/azl397985856/leetcode/master/assets/20.validParentheses.gif)

??? tip "Answer"

    ```python
    class Solution:
        def isValid(self, s: str) -> bool:
            dic = {
                ')':'(',
                '}':'{',
                ']':'['
            }
            stack = []
            for i in s:
                if stack and dic.get(i,None) == stack[-1]:
                    stack.pop()
                else:
                    stack.append(i)
            return stack == []
    ```