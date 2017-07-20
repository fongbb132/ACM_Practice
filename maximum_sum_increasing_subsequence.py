def max_inc_sub_seq(A):
    if len(A) == 0:
        return 0 

    nums = [] 
    sums = [] 
    result = 0 

    for i in A:
        isAdd = False
        for j in xrange(len(nums)):
            if i > nums[j]:
                nums[j] = i
                sums[j] += i
                result = max(sums[j], result)
                isAdd = True
        if not isAdd:
            nums.append(i)
            sums.append(i)
            result = max(result, i)

    return result
print max_inc_sub_seq([10, 5, 4, 3])

print max_inc_sub_seq([1, 101, 2, 3, 100, 4, 5])