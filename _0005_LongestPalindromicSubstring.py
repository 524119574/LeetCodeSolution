# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: "cbbd"
# Output: "bb"

"""
The runtime complexity is O(n^2) and compare this with the brute force, which is
O(n^3).
"""
class Solution(object):
    
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.low = 0
        self.high = 0

        for i in range(1, len(s)):
            self.helper(s, i, i)
            if (s[i - 1] == s[i]):
                self.helper(s, i-1, i)
        return s[self.low:self.high + 1]
        
        
    def helper(self, s, lo, hi):
        while(lo - 1 >= 0 and hi + 1 < len(s) and s[lo - 1] == s[hi + 1]):
                lo -= 1
                hi += 1
        if(hi -lo > self.high - self.low):
            self.high = hi
            self.low = lo