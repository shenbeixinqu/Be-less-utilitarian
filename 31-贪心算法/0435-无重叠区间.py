"""
给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。

 注意:

 可以认为区间的终点总是大于它的起点。
 区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。


 示例 1:

输入: [ [1,2], [2,3], [3,4], [1,3] ]
输出: 1
解释: 移除 [1,3] 后，剩下的区间没有重叠。

 示例 2:

输入: [ [1,2], [1,2], [1,2] ]
输出: 2
解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。

 示例 3:

输入: [ [1,2], [2,3] ]
输出: 0
解释: 你不需要移除任何区间，因为它们已经是无重叠的了。
 Related Topics 贪心算法
 👍 429 👎 0
 """

"""
思路:
    1.根据区间右边界进行升序排列
    2.维护right,代表已留下区间的最大右边界
    3.遍历排序后的区间
        如果当前区间的左边界>=right,该区可以留下,更新right
        如果当前区间的左边界<right,该区间去除,更新结果res
"""


def erase_overlap_intervals(intervals):
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[1])
    res = 0
    right = intervals[0][1]
    for i in range(1, len(intervals)):
        if intervals[i][0] < right:
            res += 1
        else:
            right = intervals[i][1]
    print(res)
    return res


erase_overlap_intervals([[1, 2], [2, 3]])
erase_overlap_intervals([[1, 2], [2, 3], [3, 4], [1, 3]])