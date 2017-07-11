"""
Given an integer array, your task is to find all the different possible increasing subsequences of the given array, and the length of an increasing subsequence should be at least 2 .

"""

def findSubsequences(nums):
    subs = {()}

    for n in nums:
        subs |= { a + (n, ) for a in subs if not a or a[-1] <= n}

    return [sub for sub in subs if len(sub) >= 2]


print findSubsequences([4, 6, 7, 7 ])
