"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

 网格中的障碍物和空位置分别用 1 和 0 来表示。

 示例 1：
输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
输出：2
解释：
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右

 示例 2：
输入：obstacleGrid = [[0,1],[0,0]]
输出：1

 提示：
 m == obstacleGrid.length
 n == obstacleGrid[i].length
 1 <= m, n <= 100
 obstacleGrid[i][j] 为 0 或 1
 Related Topics 数组 动态规划
 👍 551 👎 0
"""


def unique_paths_with_obstacles(grid):
    height, width = len(grid), len(grid[0])
    store = [[0] * width for _ in range(height)]
    # 从上到下,从左到右
    # 每一行
    for m in range(height):
        # 每一列
        for n in range(width):
            # 如果这一格有障碍物
            if not grid[m][n]:
                if m == n == 0:
                    store[m][n] = 1
                else:
                    a = store[m-1][n] if m != 0 else 0  # 上方格子
                    b = store[m][n-1] if n != 0 else 0  # 左方格子
                    store[m][n] = a + b
    print(store[-1][-1])
    return store[-1][-1]


unique_paths_with_obstacles([[0,0,0],[0,1,0],[0,0,0]])