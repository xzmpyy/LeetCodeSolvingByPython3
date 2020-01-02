# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
#
# 示例 1:
# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

# 示例 2:
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

# 示例 3:
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。(请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。)


class Solution:
    @staticmethod
    def length_of_longest_substring(s: str) -> int:
        # 如果字符串长度为0或空，则返回0
        if len(s) == 0 or s is None:
            return 0
        # 最长长度
        max_length = 0
        # 记录出现字符的字典
        appeared_map = {}
        # 滑块起始索引
        start = 0
        for end in range(len(s)):
            # 如果之前有重复的，且重复的在当前滑块内
            if s[end] in appeared_map.keys() and appeared_map[s[end]] >= start:
                # 若果之前有重复的，就将滑块起始位置滑至上一次出现的后一位
                start = appeared_map[s[end]] + 1
                # 将该重复字符的索引置为最新一次出现的位置
                appeared_map[s[end]] = end
            else:
                appeared_map[s[end]] = end
            if end - start + 1 > max_length:
                max_length = end - start + 1
        return max_length

