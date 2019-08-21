# 3. Longest Substring Without Repeating Characters
# Medium

# 6118

# 349

# Favorite

# Share
# Given a string, find the length of the longest substring without repeating characters.

# Example 1:

# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# Example 2:

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Note that there is no if statement when the string is empty, i.e. "".
        # This is already checked in the while loop.
        fast = slow = maxChar =0
        seen = set()
        while (fast < len(s)):
            if (s[fast] not in seen):
                seen.add(s[fast])
                fast += 1
                # The below statement only needs to execute when the fast increment, since this is the only case when `maxChar`
                # can potential increase. The other case when `slow` increases, there is no chance that the maxChar will increase.
                maxChar = max(maxChar, fast - slow)
            else:
                seen.remove(s[slow])
                slow += 1
        return maxChar
