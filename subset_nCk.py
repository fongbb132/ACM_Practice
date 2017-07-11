def subset_nCk(k, nums):
    result = [[]]
    for i in xrange(len(nums)):
        for j in xrange(len(result)):
            result.append(result[j] + [nums[i]])
        
    return [i for i in result if len(i) == k]

print subset_nCk(3, [1,2,3,4,5])
