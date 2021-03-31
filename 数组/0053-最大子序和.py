"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

 示例 1：
输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。

 示例 2：
输入：nums = [1]
输出：1

 示例 3：
输入：nums = [0]
输出：0

 示例 4：
输入：nums = [-1]
输出：-1

 示例 5：

输入：nums = [-100000]
输出：-100000

 提示：
 1 <= nums.length <= 3 * 104
 -105 <= nums[i] <= 105

 进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。
 Related Topics 数组 分治算法 动态规划
"""

'''
思路:首先，不可避免的是要遍历数组，上来就先写好for循环
遍历的同时要记录两个值：一是子数组的和tmpSum；二是子数组的和在变化过程中产生的最大值res
本题最重要的部分在于子数组的和的计算，核心代码就是
tmpSum = Math.max(tmpSum + num, num);
下面开始啰嗦地解释以上代码：
为什么是tmpSum + num 和 num 之间取最大值呢？
i. 我们可以先考虑一下什么时候tmpSum + num会小于num，也就是当前数num之前的数的和是负数的时候，如果之前的数加起来是负数，又何必要把它加上呢？直接从当前数num开始新的子数组不就好了？这种情况下tmpSum = num
ii. 那什么时候tmpSum + num会大于num呢？就是当前数num之前的数加起来是正数，因为本题并没有限制子数组的长度，只要之前的tmpSum是正数，可以增加子数组和的大小，就给它加进来。这种情况下tmpSum = tmpSum + num
子数组和tmpSum每变化一次，res都要记录一下最大值，只要大了就更新
'''


def max_sub_array(nums):
    # 子数组的和
    tmp_sum = 0
    # 和的最大值
    res = nums[0]
    for num in nums:
        tmp_sum = max(tmp_sum + num, num)
        res = max(res, tmp_sum)
    print(res)
    return res


max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4])
