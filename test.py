def two_sum(nums, target):
    hash_map = {}
    for ind, num in enumerate(nums):
        hash_map[num] = ind
    print(hash_map)


two_sum([1, 4, 4, 9], 8)