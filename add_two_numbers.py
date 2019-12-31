# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
        # 如果链表其中一个为空，则直接返回另一个
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        # 临时节点，用来作为起始，最后删除该节点
        temp_list_node = ListNode(0)
        result = temp_list_node
        # 进位
        carry = 0
        # 只要l1,或l2不为空就循环
        while l1 or l2:
            node_sum = carry
            if l1:
                node_sum += l1.val
                l1 = l1.next
            if l2:
                node_sum += l2.val
                l2 = l2.next
            # 一对节点相加后的进位
            carry = node_sum // 10
            result.next = ListNode(node_sum % 10)
            result = result.next
        # 如果循环完，还有进位，则补上进位
        if carry:
            result.next = ListNode(carry)
        # 删除链表的起始0节点
        result = temp_list_node.next
        # 结束临时节点的引用
        del temp_list_node
        return result
