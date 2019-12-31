# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]


class Solution:
    @staticmethod
    def two_sum(nums: [int], target: int) -> [int]:
        # 一个键为列表值，值为列表索引的字典
        result = {}
        length = len(nums)
        start = 0
        while start < length:
            # 如果差值在字典的键中，则取出索引，返回该索引和当前索引组成的列表
            if result.__contains__(target - nums[start]):
                return [nums.index(target - nums[start]), start]
            # 如果差值不存在，则将该列表值和索引以键值对形式存入字典
            else:
                result[nums[start]] = start
            start += 1
        return [0, 0]
