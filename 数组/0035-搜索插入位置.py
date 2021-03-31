"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

 你可以假设数组中无重复元素。

 示例 1:
 输入: [1,3,5,6], 5
输出: 2


 示例 2:
 输入: [1,3,5,6], 2
输出: 1


 示例 3:
 输入: [1,3,5,6], 7
输出: 4


 示例 4:
 输入: [1,3,5,6], 0
输出: 0

 Related Topics 数组 二分查找
"""

'''
思路:左指针 left = 0，右指针 right = n - 1
中间值 mid = (left + right) // 2，循环条件 left <= right
当 nums[mid] = target 时，找到目标，返回mid
当 nums[mid] > target 时，说明当前值偏大，右指针左移至 mid - 1
当 nums[mid] < target 时，说明当前值偏小，左指针右移至 mid + 1
跳出循环时，left 指向 target 插入位置，返回 left
'''


def search_insert(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    print(left)
    return left


search_insert([1, 3, 5, 6], 7)


