"""
给定一个三角形 triangle ，找出自顶向下的最小路径和。
 每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。也就是说，如果
正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。

 示例 1：
输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
输出：11
解释：如下面简图所示：
   2
  3 4
 6 5 7
4 1 8 3
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

 示例 2：
输入：triangle = [[-10]]
输出：-10
 提示：
 1 <= triangle.length <= 200
 triangle[0].length == 1
 triangle[i].length == triangle[i - 1].length + 1
 -104 <= triangle[i][j] <= 104

 进阶：
 你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题吗？
 Related Topics 数组 动态规划
 👍 763 👎 0
"""

"""
思路:
    动态规划,保证每一层每个位置的最小路径和
    1.特判, 若triangle为空,返回0,若只有一层len(triangle)==1,返回元素本身
    2.从第二行开始,遍历区间[1,n)
        对每一层进行遍历,存在三种情况
        (1).每一行的首位,triangle[i][j] += triangle[i-1][j],等于上一行的相同索引处
        (2).每一行的末位,triangle[i][j] += triangle[i-1][j-1],等于上一行的前一位处
        (3).对于其他元素,triangle[i][j] += min(triangle[i-1][j-1],triangle[i-1][j]),
            等于上一行中相邻的较小值加上自身
    3.返回最后一行中的最小路径和
"""


def mini_mum_total(triangle):
    if not triangle:
        return 0
    n = len(triangle)
    if n == 1:
        return triangle[0][0]
    for i in range(1, n):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
    print(min(triangle[-1]))
    return min(triangle[-1])


mini_mum_total([[2],[3,4],[6,5,7],[4,1,8,3]])