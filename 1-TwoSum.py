# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

"""
Note:
Firstly, the run time can be O(n). And note that you may not use the same element twice, so do check for that.
"""

# Below is the first iteration of solution, however not that this is not fast enought, since we run through the loop twice. This is O(n) algorithm,
# however we should still strive to reduce the constant.
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mem = dict()
        for i in range(len(nums)):
            mem[nums[i]] = i
        for i in range(len(nums)):
            remain = target - nums[i]
            if (remain in mem and mem[remain] != i):
                return [i, mem[remain]]

# A better version is the following, note that in the following version, I don't need to check that we are using different elements,
# plus the fact that we only need to iterate it through once:
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = dict()
        for i in range(len(nums)):
            diff = target - nums[i]
            if (diff in seen):
                return [seen[diff], i]
            else:
                seen[nums[i]] = i
