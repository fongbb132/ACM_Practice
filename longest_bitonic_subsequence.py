"""
Bitonic if it is first increasing, then decreasing.

"""

def lbs(arr):
    print arr
    if not arr:
        return 0 
    l = len(arr)
    lis = [1 for i in xrange(l+1)]
    lds = [1 for i in xrange(l+1)]

    for i in xrange(1, l):
        for j in xrange(0, i):
            if arr[i] > arr[j]:
                lis[i] = max(lis[i], lis[j] + 1) 
            if arr[l-i-1] > arr[l-j-1]:
                lds[i] = max(lds[i], lds[j] + 1)

    result = 0 
    for (a,b) in zip(lis, lds):
        result = max(result, a+b-1)
    return result

print lbs([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5,13, 3, 11, 7, 15])
print lbs([12, 11, 40, 5, 3, 1])
print lbs([1, 11, 2, 10, 4, 5, 2, 1])
print lbs([80, 60, 30, 40, 20, 10])


