### 应用动态规划
```
1.建立转移方程
    如:已经知道f(1)~f(n-1)的值,求f(n)
2.缓存并复用以往结果
3.按顺序从小到大算
```

思想:
    递归加缓存

### 如何解决动态规划问题
```
四步法
- 判别是不是一个动态规划问题
- 确定状态
- 建立状态之间的关系
- 为状态添加dptable
第一步
    一般情况下,需要求最优解的时候(最短路径,最长公共子序列,最大字段和等等,
出现最字就要留意),在一定条件下对排列进行计数的计数问题(丑数问题)或
某些概率问题都可以考虑用动态规划来解决

第二步
    DP 问题最重要的就是确定所有的状态和状态与状态之间的转移方程。
确定状态转移方程是动态规划最难的部分，但也是最基础的，必须非常谨慎地选择状态，
因为状态转移方程的确定取决于对问题状态定义的选择

第三步
    构造状态转移方程是dp最难的部分

第四步
    仅需存储子状态的解,以便下次使用子状态时直接查表从内存中获得
```

### 矩阵问题
```
方式1:
data = [[0]*3]*4   #4行3列
print(data) #[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
data[0][0] = 1
print(data) #[[1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]]
方式2:
data1 = [[0 for i in range(3)] for j in range(4)]
print(data)#[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
data[0][0] = 1
print(data) #[[1, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

dp1 = [[0] * (n + 1) for _ in range(m + 1)]
# [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
dp2 = [[0 for j in range(4)] for i in range(2)]
# [[0, 0, 0, 0], [0, 0, 0, 0]]
```
