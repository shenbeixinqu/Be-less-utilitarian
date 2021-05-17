def fib(n):
    # 用于缓存以往结果,以便复用(目标2)
    results = list(range(n+1))
    # 按顺序从小到大算(目标3)
    for i in range(n+1):
        if i < 2:
            results[i] = i
        else:
            # 使用状态方程(目标1), 同时复用以往结果(目标2)
            results[i] = results[i - 1] + results[i - 2]
    print(results[-1])
    return results[-1]


fib(1)
