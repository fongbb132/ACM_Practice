def lcs(s,y):
    if not s or not y:
        return 0
    if s[-1] == y[-1]:
        return 1 + lcs(s[0:-1], y[0:-1])
    else:
        return max(lcs(s[0:-1], y), lcs(s, y[0:-1]))


def lcs2(s, y):
    m, n = len(s)+1, len(y)+1
    dp = [[0]*n]*m
    for i in xrange(1, m, 1):
        for j in xrange(1, n, 1):
            if s[i-1] == y[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m-1][n-1]
print lcs2("AGGTAB",  "GXTXAYB")
