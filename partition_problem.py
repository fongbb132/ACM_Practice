def partition(arr):
    s = 0
    for i in arr:
        s += i

    if s %2 == 1:
        return False
    
    dp = [[False for i in range(len(arr)+1)]for j in range(s/2+1)]

    dp[0][0] = True

    for i in xrange(s/2):
        dp[i][0] = True
    
    for i in xrange(1,s/2+1):
        for j in xrange(1,len(arr)+1):
            dp[i][j] = dp[i][j-1]
            if arr[j-1] < i :
                dp[i][j] = dp[i][j] or dp[i - arr[j-1]][j-1]
    return dp[s/2][len(arr)]
print partition([3,1,1,2,2,1])
