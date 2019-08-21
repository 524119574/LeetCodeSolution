# 2. Add Two Numbers
# Medium

# 5778

# 1486

# Favorite

# Share
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

"""
Test cases:
(2->4->3) + (0)

342 + 0 = 342

The slightly tricky part is how to handle the numbers that are of different length.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        left, right = l1, l2
        sumNode = cur = ListNode(0)
        dummyHead = ListNode(0)
        while (left != dummyHead or right != dummyHead):
            (carry, mod) = divmod(left.val + right.val + carry, 10)
            cur.next = ListNode(mod)
            cur = cur.next
            left = left.next if left.next else dummyHead
            right = right.next if right.next else dummyHead
            
        if (carry == 1):
            cur.next = ListNode(1)
        return sumNode.next


