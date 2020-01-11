# 双指针


## 首尾双指针
一般用于寻找数组/双向链表中满足条件的 **两个节点**；如果是寻找多个数，则先固定前 n-2 个数


- 确保有序 list.sort()
- while 循环
- 双指针初始化
- 迭代
- 去重复

### [翻转字符串](https://leetcode.com/problems/reverse-string/)

!!! question "翻转字符串"

    Write a function that reverses a string. The input string is given as an array of characters char[].

    Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

    You may assume all the characters consist of printable ascii characters.

??? tip "Answer"

    ```python
    class Solution:
        def reverseString(self, s: List[str]) -> None:
            """
            Do not return anything, modify s in-place instead.
            """
            left, right = 0, len(s)-1
            while left < right:
                s[left],s[right] = s[right],s[left]
                left += 1
                right -= 1
    ```

### [两数之和](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

!!! question "两数之和"
    给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

    函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

    说明:

    返回的下标值（index1 和 index2）不是从零开始的。
    你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
    示例:
    ```
    输入: numbers = [2, 7, 11, 15], target = 9
    输出: [1,2]
    解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
    ```

??? tip "Answer 1: Two Pointers"

    ```python

    class Solution:
        def twoSum(self, numbers: List[int], target: int) -> List[int]:
            n = len(numbers)
            lo,hi = 0, n-1
            while lo < hi:
                s = numbers[lo] + numbers[hi]
                if s > target:
                    hi -= 1
                elif s < target:
                    lo += 1
                else:
                    return lo+1,hi+1
    ```

??? tip "Answer 2: Dict"

    ```python
    class Solition:
        def twoSum2(self, numbers, target):
            dic = {}
            for i, num in enumerate(numbers):
                if target-num in dic:
                    return [dic[target-num]+1, i+1]
                dic[num] = i
    ```
    
### [三数之和](https://leetcode.com/problems/3sum/description/)

!!! question "三数之和"
    
    给定一个包含 n 个整数的数组 nums，
    判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？
    找出所有满足条件且不重复的三元组。

    注意：答案中不可以包含重复的三元组。

    例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

    满足要求的三元组集合为：
    ```
    [
    [-1, 0, 1],
    [-1, -1, 2]
    ]
    ```

??? tip
    - 排序 + 首尾双指针
    - 将第三个数当作前两个数的目标和，在两数之和的基础上套一层循环
    - 难点在于如何 **去重**（不借用 set）


??? tip "Answer"

    ```python

    class Solution:
        def threeSum(self, nums: List[int]) -> List[List[int]]:
            nums.sort() # 首先排序
            n = len(nums)
            res = []
            for i in range(n-2):
                if i > 0 and nums[i] == nums[i-1]: # 对第一个数去重
                    continue
                target = -nums[i]
                lo, hi = i + 1, n - 1
                while lo < hi:
                    s = nums[lo] + nums[hi]
                    if s > target:
                        hi -= 1
                    elif s < target:
                        lo += 1
                    else:
                        res.append([nums[i],nums[lo],nums[hi]])
                        lo += 1 # 先移指针
                        while lo < hi and nums[lo] == nums[lo - 1]: # 再去重
                            lo += 1
            return res
    ```
    
### [最接近的三数之和](https://leetcode.com/problems/3sum-closest/description/)

!!! question "最接近的三数之和"
    
    给定一个包括 n 个整数的数组 nums 和 一个目标值 target。
    找出 nums 中的三个整数，使得它们的和与 target 最接近。
    返回这三个数的和。假定每组输入只存在唯一答案。

    例如，给定数组 `nums = [-1，2，1，-4]`, 和 `target = 1`.

    与 target 最接近的三个数的和为 2.` (-1 + 2 + 1 = 2)`.

??? tip
    - 排序 + 双指针
    - 更接近：差的绝对值更小

??? tip "Answer"

    ```python
    class Solution:
        def threeSumClosest(self, nums: List[int], target: int) -> int:
            nums.sort() # 先排序
            n = len(nums)
            closest = nums[0] + nums[1] + nums[2] # 用一个特殊值初始化
            
            for i in range(n-2):
                if i > 0 and nums[i] == nums[i-1]: # 第一个数去重
                    continue
                lo, hi = i+1, n-1 # 首尾双指针
                while lo < hi:
                    s = nums[i] + nums[lo] + nums[hi]
                    if abs(s-target) < abs(closest-target): # 更接近
                        closest = s
                    if s > target:
                        hi -= 1
                    elif s < target:
                        lo += 1
                    else:
                        return target
            return closest
    ```

### [两数之和 - 小于等于目标值的个数](https://blog.csdn.net/qq_36387683/article/details/81460276)

!!! question "两数之和 - 小于等于目标值的个数"
    给定一个整数数组，找出这个数组中有多少对的和是小于或等于目标值。返回对数。

    样例
    ```

        给定数组为 [2,7,11,15]，目标值为 24
        返回 5。
        2+7<24
        2+11<24
        2+15<24
        7+11<24
        7+15<24
    ```

??? tip
    - 排序 + 首尾双指针
    - 根据条件判断迭代增幅

??? tip "Answer"

    ```python
    def solution(nums:list,target:int)->int:
        nums.sort() # 首尾双指针一般要求有序
        n = len(nums)
        lo, hi = 0, n-1
        res = 0
        while lo < hi: 
            s = nums[lo] + nums[hi]
            if s > target:
                hi -= 1
            else:
                res += hi - lo # 若最小和最大的和小于目标，则最小和其他和一定都小于目标，故每次递增hi-lo
                lo += 1
        return res
    ```

### [三数之和 - 小于等于目标值的个数](https://www.lintcode.com/problem/3sum-smaller/description)

!!! question "三数之和 - 小于等于目标值的个数"
    
    给定一个n个整数的数组和一个目标整数target，
    找到下标为i、j、k的数组元素`0 <= i < j < k < n`，满足条件`nums[i] + nums[j] + nums[k] < target.`

    样例
    给定 `nums = [-2,0,1,3], target = 2,` 返回 2.

    解释:
    ```
        因为有两种三个元素之和，它们的和小于2:
        [-2, 0, 1]
        [-2, 0, 3]
    ```

??? tip
    - 排序 + 双指针

??? tip "Answer"

    ```python
    class Solution:
    """
    @param nums:  an array of n integers
    @param target: a target
    @return: the number of index triplets satisfy the condition nums[i] + nums[j] + nums[k] < target
    """
    def threeSumSmaller(self, nums, target):
        # Write your code here
        n = len(nums)
        nums.sort()
        res = 0
        
        for i in range(n-2):
            lo, hi = i+1, n-1
            while lo < hi:
                s = nums[i] + nums[lo] + nums[hi]
                if s < target:
                    res += hi - lo
                    lo += 1
                else:
                    hi -= 1
        return res
    ```
### [三角形计数 Valid Triangle Number](https://leetcode-cn.com/problems/valid-triangle-number/description/)

!!! question "三角形计数"

    给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形三条边的三元组个数。
    ```
    示例 1:
        输入: [2,2,3,4]
        输出: 3
    解释:
        有效的组合是: 
        2,3,4 (使用第一个 2)
        2,3,4 (使用第二个 2)
        2,2,3
    注意:
        数组长度不超过1000。
        数组里整数的范围为 [0, 1000]。
    ```

??? tip
    - 排序 + 首尾双指针
    - 相当于两数之和大于目标值的个数
    - 我们先对这个数组进行排序，排序之后我们来指出这个三角形中最长的边，那么剩下两条边的要求是：两边之和大于最长边。
    - 所以，我们只需要对最长边进行变遍历，对两个短边再遍历即可。
    - 短边的遍历方法是：一个从0开始的短边 `lo`，一个从比最长边的短的一个边 `hi` 开始向中间遍历。如果能够成三角形，那么说明比`lo`长的短边和`hi`结合也都能组成三角形。如果不能组成三角形，那么说明`lo`太小了，需要向中间移动。
    - 排序算法时间复杂度是O(nlogn)，for循环时间复杂度为O(n)，while循环虽然有两个变量，但是这两个变量是同时向中间移动的关系，所以时间复杂度不会超过O(n)，总体的时间复杂度是O(n)。空间复杂度是O(1)。

??? tip "Answer"

    ```python
    class Solution:
        def triangleNumber(self, A):
            """
            :type A: List[int]
            :rtype: int
            """
            A.sort()
            n = len(A)
            
            cnt = 0
            for i in range(2, n):  # 注意：循环区间,保证了两边之差一定小于第三边
                
                lo, hi = 0, i - 1
                while lo < hi:
                    s = A[lo] + A[hi]
                    
                    if s > A[i]:
                        cnt += hi - lo
                        hi -= 1
                    else:
                        lo += 1
                        
            return cnt
    ```

### [接雨水 Trapping Rain Water 一维](https://leetcode-cn.com/problems/trapping-rain-water/description/)

!!! question "接雨水 Trapping Rain Water 一维"
    
    给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
    ```
    示例:
        输入: [0,1,0,2,1,0,1,3,2,1,2,1]
        输出: 6
    ```
??? tip
    - 双指针，遍历一次数组
    - 一个位置可装水的量由 `它左右最低的木板-自身高度` 决定
    - [视频讲解](https://www.bilibili.com/video/av18241289/?spm_id_from=333.788.videocard.1)

??? tip "Answer"

    ```python

        class Solution:
            def trap(self, height: List[int]) -> int:
                n = len(height)
                left, right = 0, n-1 # 初始化指针
                max_left = max_right= 0 # 初始化左右最高高度[左右木板]   
                res = 0 # 初始化答案
                while left <= right: # 直到左右指针相遇
                    if height[left] <= height[right]: # 若右指针对应高度更高 -> 处理左边：木桶效应，可以装的雨水由最短的一边确定。
                        if height[left] > max_left: # 若左指针对应高度比当前左木板更高
                            max_left = height[left] # 则该块充当左边木板，更新左木板高度
                        else:
                            res += max_left - height[left] # 否则，该块可以装雨水；量：左边木板-该块高度
                        left += 1 # 向右逼近
                    elif height[left] > height[right]: # 若左指针对应高度更高 -> 处理右边：木桶效应，可以装的雨水由最短的一边确定。
                        if height[right] > max_right: # 若右指针对应高度比当前右木板更高
                            max_right = height[right] # 则该块充当右边木板，更新右木板高度
                        else:
                            res += max_right - height[right] # 否则，该块可装雨水；量：右木板高度-该块高度 
                        right -= 1 # 向左逼近
                return res
    ```

### [盛最多水的容器 Container With Most Water](https://leetcode.com/problems/container-with-most-water/description/)

!!! question "盛最多水的容器"
    给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
    说明：你不能倾斜容器，且 n 的值至少为 2。
    ```
    示例:
        输入: [1,8,6,2,5,4,8,3,7]
        输出: 49
    ```

??? tip
    - 首尾双指针
    - 注意由于水的连通性（木桶效应），水的面积是 `底边 * 最短的竖边`
    - 双指针根据竖边的高低进行迭代，具体面积大小需再判断后再替换。

??? tip "Answer"

    ```python
    class Solution:
        def maxArea(self, height: List[int]) -> int:
            left, right = 0, len(height) - 1 # 初始化指针
            res = (right - left) * min(height[left],height[right]) # 初始化面积

            while left < right: # 直到两指针相遇
                if height[left] < height[right]: # 若右指针更高
                    left += 1 # 向右逼近
                else: # 若左指针更高
                    right -= 1 # 向左逼近
                
                area = (right-left) * min(height[right],height[left]) # 当前面积
                if area > res: res = area # 若更大，则更新最大面积
            return res
    ```

### [颜色分类](https://leetcode.com/problems/sort-colors/)

!!! question "颜色分类"

    给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

    此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

    注意:
    不能使用代码库中的排序函数来解决这道题。

    示例:
    ```
    输入: [2,0,2,1,1,0]
    输出: [0,0,1,1,2,2]
    ```

    进阶：
    一个直观的解决方案是使用计数排序的两趟扫描算法。
    首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
    你能想出一个仅使用常数空间的一趟扫描算法吗？

??? tip 
    - 首尾双指针
        - `l` 记录最后一个 0 的位置
        - `r` 记录第一个 2 的位置
        - `i` 表示当前遍历的元素

??? tip "Answer"
    
    ```python
    class Solution:
        def sortColors(self, A):
            """
            :type A: List[int]
            :rtype: void Do not return anything, modify A in-place instead.
            """
            n = len(A)
            
            l = 0  # l 指示最后一个 0
            r = n - 1  # r 指示第一个 2
            
            i = 0
            while i <= r:
                if A[i] == 0:
                    A[i] = A[l]
                    A[l] = 0  # 确定最后一个 0
                    l += 1
                if A[i] == 2:
                    A[i] = A[r]
                    A[r] = 2  # 确定第一个 2
                    r -= 1
                    i -= 1  # 注意回退，因为不确定原 A[r] 处是什么
                i += 1
    ```
