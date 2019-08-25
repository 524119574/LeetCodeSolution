# 380. Insert Delete GetRandom O(1)
# Medium

# 1277

# 95

# Favorite

# Share
# Design a data structure that supports all following operations in average O(1) time.

# insert(val): Inserts an item val to the set if not already present.
# remove(val): Removes an item val from the set if present.
# getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
# Example:

# // Init an empty set.
# RandomizedSet randomSet = new RandomizedSet();

# // Inserts 1 to the set. Returns true as 1 was inserted successfully.
# randomSet.insert(1);

# // Returns false as 2 does not exist in the set.
# randomSet.remove(2);

# // Inserts 2 to the set, returns true. Set now contains [1,2].
# randomSet.insert(2);

# // getRandom should return either 1 or 2 randomly.
# randomSet.getRandom();

# // Removes 1 from the set, returns true. Set now contains [2].
# randomSet.remove(1);

# // 2 was already in the set, so return false.
# randomSet.insert(2);

# // Since 2 is the only number in the set, getRandom always return 2.
# randomSet.getRandom();

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = set()

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if (val in self.nums):
            return False
        self.nums.add(val)
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if (val in self.nums):
            self.nums.discard(val)
            return True
        else:
            self.nums.discard(val)
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        temp = list(self.nums)
        idx = random.randint(0, len(temp) - 1)
        return temp[idx]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

"""
Note that the above solution doesn't satisfy the requirement, since the conversion from set to list is not O(1).

The below solution satisfies the requirements. The idea is to keep a list of numbers, and keep a mapping from the number to their index in the list.

Possible Follow-up:
Currently, we don't allow the numbers to be duplicated, what if we allow the numbers to be duplicated? How do we still achieve the O(1)
time complexity.

Ans:
Instead of using a map between integer(val) to integer(index), we should use a map that maps from integer(val) to set(a set of index).

"""

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = list()
        self.pos = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if (val in self.pos):
            return False
        self.pos[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if (val in self.pos):
            idx, lastVal = self.pos[val], self.nums[-1]
            self.pos[lastVal], self.nums[idx] = idx, lastVal  # Move the last element to the position of `val`.
            self.nums.pop(), self.pos.pop(val)                # Then remove the last element.
            return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.nums[random.randint(0, len(self.nums) - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
