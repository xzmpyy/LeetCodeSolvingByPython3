# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
# 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
# 你可以假设 nums1 和 nums2 不会同时为空。
#
# 示例 1:
# nums1 = [1, 3]
# nums2 = [2]
# 则中位数是 2.0
#
# 示例 2:
# nums1 = [1, 2]
# nums2 = [3, 4]
# 则中位数是 (2 + 3)/2 = 2.5


class Solution:
    @staticmethod
    def find_median_sorted_arrays(nums1: [int], nums2: [int]) -> float:
        m, n = len(nums1), len(nums2)
        # 若其中一个数组为空，则直接返回另一个数组的中位数
        if m == 0 or nums1 is None:
            if n % 2 == 1:
                return nums2[int(n/2)]
            else:
                return (nums2[int(n/2)] + nums2[int(n/2) - 1])/2
        if n == 0 or nums2 is None:
            if m % 2 == 1:
                return nums1[int(m/2)]
            else:
                return (nums1[int(m/2)] + nums1[int(m/2) - 1])/2
        if m == 1 and n == 1:
            return (nums1[0] + nums2[0])/2
        # 两个数组总长度奇偶性
        even_odd = (m + n) % 2
        # 不断比较两个数组的第一位和最后一位，让小的和大的被移除，留下中位数
        while True:
            if nums1[0] <= nums2[0]:
                nums1.pop(0)
                m -= 1
            else:
                nums2.pop(0)
                n -= 1
            if m == 0:
                while True:
                    nums2.pop(n-1)
                    n -= 1
                    if n == 2 and even_odd == 0:
                        return (nums2[0] + nums2[1])/2
                    if n == 1 and even_odd == 1:
                        return nums2[0]
                    nums2.pop(0)
                    n -= 1
            if n == 0:
                while True:
                    nums1.pop(m - 1)
                    m -= 1
                    if m == 2 and even_odd == 0:
                        return (nums1[0] + nums1[1]) / 2
                    if m == 1 and even_odd == 1:
                        return nums1[0]
                    nums1.pop(0)
                    m -= 1
            if nums1[m-1] >= nums2[n-1]:
                nums1.pop(m-1)
                m -= 1
            else:
                nums2.pop(n-1)
                n -= 1
            if m == 0:
                while True:
                    if n == 2 and even_odd == 0:
                        return (nums2[0] + nums2[1]) / 2
                    if n == 1 and even_odd == 1:
                        return nums2[0]
                    nums2.pop(0)
                    n -= 1
                    nums2.pop(n - 1)
                    n -= 1
            if n == 0:
                while True:
                    if m == 2 and even_odd == 0:
                        return (nums1[0] + nums1[1]) / 2
                    if m == 1 and even_odd == 1:
                        return nums1[0]
                    nums1.pop(0)
                    m -= 1
                    nums1.pop(m - 1)
                    m -= 1
            if m == 1 and n == 1 and even_odd == 0:
                return (nums1[0] + nums2[0])/2

