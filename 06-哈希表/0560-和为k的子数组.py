"""
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

 示例 1 :
输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。

 说明 :
 数组的长度为 [1, 20,000]。
 数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。

 Related Topics 数组 哈希表
 👍 895 👎 0
"""

"""
解题思路:
    前缀和,保存一个数组的前缀和,然后利用差分法得出任意区间段的和
"""


def subarray_sum(nums, k):
    dic = {}
    acc, res = 0, 0
    for num in nums:
        acc += num
        if acc == k:
            res += 1
        if acc - k in dic:
            res += dic[acc - k]
        dic[acc] = dic.get(acc, 0) + 1
    print(res)
    return res


subarray_sum([1, 2, 3, 3, 3, 1, 2], 6)

