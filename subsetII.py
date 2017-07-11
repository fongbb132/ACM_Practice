"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets.
"""

def subsetWithDup(nums):
    result = [[]]
    nums.sort()

    for i in xrange(len(nums)):
        if i == 0 or nums[i] != nums[i-1]:
            l = len(result)

        for j in xrange(len(result) - l , len(result)):
            result.append(result[j] + [nums[i]])

    return result


print subsetWithDup([1,2,2,3])
