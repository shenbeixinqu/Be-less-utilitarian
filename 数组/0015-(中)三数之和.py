"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重
复的三元组。
 注意：答案中不可以包含重复的三元组。

 示例 1：
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]

 示例 2：
输入：nums = []
输出：[]

 示例 3：
输入：nums = [0]
输出：[]

 提示：
 0 <= nums.length <= 3000
 -105 <= nums[i] <= 105

 Related Topics 数组 双指针
"""


def three_sum(nums):
    nums.sort()
    res, k = [], 0
    for k in range(len(nums) - 2):
        if nums[k] > 0:
            break
        if k > 0 and nums[k] == nums[k-1]:
            continue
        i, j = k+1, len(nums)-1
        while i < j:
            s = nums[k] + nums[i] + nums[j]
            if s < 0:
                i += 1
                while i < j and nums[i] == nums[i-1]:
                    i += 1
            elif s > 0:
                j -= 1
                while i < j and nums[j] == nums[j+1]:
                    j -= 1
            else:
                res.append([nums[k], nums[i], nums[j]])
                i += 1
                j -= 1
                while i < j and nums[i] == nums[i - 1]:
                    i += 1
                while i < j and nums[j] == nums[j + 1]:
                    j -= 1
    return res


three_sum()
