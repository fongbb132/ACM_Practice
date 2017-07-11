def lis(arr):
    n = len(arr)
    dp = [1]*n

    for i in xrange(1, n , 1):
        for j in xrange (i):
            if arr[i] > arr[j] and dp[j] >= dp[i]:
                dp[i] = dp[j] + 1
    _max = 0 
    for i in dp:
        _max = max(i, _max) 
    return _max

a = [3, 10, 2, 1, 20]
print lis(a)
