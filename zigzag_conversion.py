# 将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
# 比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
# L   C   I   R
# E T O E S I I G
# E   D   H   N
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
# 请你实现这个将字符串进行指定行数变换的函数：
# string convert(string s, int numRows);

# 示例 1:
# 输入: s = "LEETCODEISHIRING", numRows = 3
# 输出: "LCIRETOESIIGEDHN"

# 示例 2:
# 输入: s = "LEETCODEISHIRING", numRows = 4
# 输出: "LDREOEIIECIHNTSG"
# 解释:
# L     D     R
# E   O E   I I
# E C   I H   N
# T     S     G


class Solution:
    @staticmethod
    def convert(s: str, num_rows: int) -> str:
        # 如果只有一行，直接返回该字符串
        if num_rows == 1:
            return s
        # 用于存储当前坐标点的变量
        x = 0
        # 代表坐标系的多维数组
        coordinates = []
        result = ""
        # 标记该列是否只有一个字符的标识
        single_flag = False
        for _ in range(num_rows):
            coordinates.append([])
        for letter in s:
            if single_flag:
                coordinates[x].append(letter)
                if x == 0:
                    single_flag = False
            else:
                coordinates[x].append(letter)
            if x == num_rows - 1:
                single_flag = True
                x -= 1
            elif single_flag:
                x -= 1
            else:
                x += 1
        for arr in coordinates:
            for c in arr:
                result += c
        return result
