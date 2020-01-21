# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
#
# 示例 1:
# 输入: 121
# 输出: true

# 示例 2:
# 输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

# 示例 3:
# 输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。

# 进阶:
# 你能不将整数转为字符串来解决这个问题吗？


class Solution:
    @staticmethod
    def is_palindrome(x: int) -> bool:
        if x < 0:
            return False
        elif 0 <= x < 10:
            return True
        else:
            revers = 0
            temp = x
            while temp > 0:
                revers = revers*10 + temp % 10
                temp = int(temp / 10)
            return revers == x
