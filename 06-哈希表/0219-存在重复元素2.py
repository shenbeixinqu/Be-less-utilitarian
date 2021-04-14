"""
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值
 小于等于k。

 示例 1:
 输入: nums = [1,2,3,1], k = 3
输出: true

 示例 2:
 输入: nums = [1,0,1,1], k = 1
输出: true

 示例 3:
 输入: nums = [1,2,3,1,2,3], k = 2
输出: false
 Related Topics 数组 哈希表
 👍 254 👎 0
"""

"""
思路:用字典保存值和索引,if代码后半句:如果值存在且索引差小于k 
i - dct[nums[i]] <= k
"""


def contain_duplicate(nums, k):
    dct = {}
    for i in range(len(nums)):
        if nums[i] in dct and dct[nums[i]] >= i - k:
            return True
        dct[nums[i]] = i
    return False


contain_duplicate([1,0,1,1],1)
