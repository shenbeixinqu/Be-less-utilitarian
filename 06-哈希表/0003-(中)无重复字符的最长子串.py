"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
 示例 1:
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

 示例 2:
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

 示例 3:
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

 示例 4:
输入: s = ""
输出: 0

 提示：
 0 <= s.length <= 5 * 104
 s 由英文字母、数字、符号和空格组成

 Related Topics 哈希表 双指针 字符串 Sliding Window
 👍 5323 👎 0
"""
'''
思路: #36 i,c 分别为索引和键
'''


def longest_substring(nums):
    start, res, n_dic = -1, 0, {}
    for i, c in enumerate(nums):
        if c in n_dic and n_dic[c] > start:
            start = n_dic[c]
            n_dic[c] = i
        else:
            n_dic[c] = i
            res = max(res, i-start)

    print(res)
    return res


longest_substring("pwwkew")