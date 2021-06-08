"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。

示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

示例 2：
输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]

提示：

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
"""

"""
    思路:
        我们遍历到数字a时,用target减去a,就会得到b,若b存在哈希表中,我们可以直接返回结果
        若b不存在,我们需要将a存入哈希表,好让后续遍历的数字使用
"""


def two_sum(nums, target):
    hashtable = dict()
    for i, num in enumerate(nums):
        if target - num in hashtable:
            print([hashtable[target-num], i])
            return [hashtable[target-num], i]
        hashtable[num] = i
    print([])
    return []


# two_sum([2, 7, 11, 15], 14)
two_sum([3, 3, 3], 6)
