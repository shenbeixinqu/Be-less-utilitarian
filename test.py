# 1.二维数组
# def digui(grip):
#     z = grip[0]
#     print(z)
#     m, n = len(grip[0]), len(grip)
#     print(m, n)
#     dp = [1] + [0] * m
#     print(dp)
#     dp1 = [[0] * (n + 1) for _ in range(m + 1)]
#     dp2 = [[0] * m] * n
#     dp3 = [[0 for j in range(n)] for i in range(m)]
#     print(dp1)
#     print(dp2)
#     print(dp3)
#     dp2[0][0] = 1
#     print(dp2)
#     dp3[0][0] = 1
#     print(dp3)
#
# digui( [[0,0,0],[0,1,0],[0,0,0]])


#  2.lambda变量

add = lambda x, y: x+y
print(add(1, 2))
