from collections import Counter


def two_sum(nums, target):
    hash_map = {}
    for ind, num in enumerate(nums):
        hash_map[num] = ind
    print(hash_map)


def is_anagram(s):
    d_dict = Counter(s)
    print(d_dict)


# two_sum([1, 4, 4, 9], 8)
is_anagram("anangram")