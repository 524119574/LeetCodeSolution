"""
Word coAppearence:

Given a list of words ["abc", "bcd", "def"]

Output the characters that appears the most often with other characters

{
'a': ['b', 'c'],
'b': ['c'],  # note that 'a', 'd' only coappear with b once, while c coappear twice
'c': ['b'],
'd': ['b', 'c', 'e', 'f'],
'e': ['d', 'f'],
'f': ['e', 'd'],
}

My final answer is the following:

"""

def findCoAppear(words):
    mapping = {}
    for word in words:
        for c1 in word:
            counts = mapping.get(c1, {})
            for c2 in word:
                if (c1 != c2):
                    counts[c2] = counts.get(c2, 0) + 1
            mapping[c1] = counts
    finalRes = {}
    for ch, counts in mapping.items():
        res = []
        maxCount = max(counts.values())
        for key, count in mapping[ch].items():
            if (count == maxCount):
                res.append(key)
        finalRes[ch] = res
    return finalRes

print(findCoAppear(["abc", "bcd", "def"]))