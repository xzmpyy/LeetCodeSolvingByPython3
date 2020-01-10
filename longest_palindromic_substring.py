# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
# 回文字符串即正读和反读均相同的字符串
# 示例 1：
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
#
# 示例 2：
# 输入: "cbbd"
# 输出: "bb"


class Solution:
    @staticmethod
    def longest_palindrome(s: str) -> str:
        # 如果长度小于等于1，则直接返回自身
        if len(s) <= 1:
            return s
        longest_string = ""
        # 在每一个字符两边插入#，保证除第一个#和最后一个#外每个点都可以成为中心点，左右均有值
        # 例如"babad"生成"#b#a#b#a#d#"
        temp = "#"
        for i in s:
            temp += i + "#"
        # 步长，及回文子串的最长半径
        strip = 1
        # 遍历除第一个#和最后一个#外的所有点的索引
        for i in range(1, len(temp) - 2):
            # 若该点左右两端加上步长后仍在字符串内
            # 且左边等右边的反转,[::-1]是将字符串反转
            # 则该子串为回文子串
            while i - strip >= 0 and i + strip < len(temp) and \
                    temp[i - strip:i + strip + 1] == temp[i - strip:i + strip + 1][::-1]:
                longest_string = temp[i - strip:i + strip + 1]
                # 将步长加一，继续向外扩展，验证以该点为中心是否存在更长子串
                strip += 1
        result = ""
        # 去掉原先添加的#
        for i in longest_string:
            if i != '#':
                result += i
        return result


if __name__ == '__main__':
    print(Solution.longest_palindrome("aaabcaaa"))
