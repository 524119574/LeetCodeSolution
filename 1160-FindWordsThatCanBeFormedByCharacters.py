# You are given an array of strings words and a string chars.

# A string is good if it can be formed by characters from chars (each character can only be used once).

# Return the sum of lengths of all good strings in words.

 

# Example 1:

# Input: words = ["cat","bt","hat","tree"], chars = "atach"
# Output: 6
# Explanation: 
# The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
# Example 2:

# Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
# Output: 10
# Explanation: 
# The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
 

# Note:

# 1 <= words.length <= 1000
# 1 <= words[i].length, chars.length <= 100
# All strings contain lowercase English letters only.

"""
This is a Leetcode contest question, quite easy, just record the occurence of each character and then check.
Just don't be afraid to copy the set and modify the copied verison.
"""

class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        mem = dict()
        for char in chars:
            mem[char] = mem.get(char, 0) + 1
        totalSize = 0
        for word in words:
            if (self.isGoodStr(word, mem)):
                totalSize += len(word)
        return totalSize
        
    def isGoodStr(self, word, mem):
        memNew = mem.copy()
        for c in word:
            if (c not in memNew or memNew[c] <= 0):
                return False
            else:
                memNew[c] = memNew[c] - 1
        return True
