"""
Suppose that we wish to know which stories in a 36-story building are safe to drop eggs from, and which will cause the eggs to break on landing. We make a few assumptions:

An egg that survives a fall can be used again.
A broken egg must be discarded.
The effect of a fall is the same for all eggs.
If an egg breaks when dropped, then it would break if dropped from a higher floor.
If an egg survives a fall then it would survive a shorter fall.
It is not ruled out that the first-floor windows break eggs, nor is it ruled out that the 36th-floor do not cause an egg to break.

Function to get minimum number of trials needed in worst
case with n eggs and k floors 
"""

def egg_drop_puzzle(n, k):
    if k == 1 or k == 0 :
        return k

    if n == 1:
        return k
    _min = 10**10
    for i in xrange(1, k+1):
        res = max(egg_drop_puzzle(n-1, i-1), egg_drop_puzzle(n, k-i))
        if res < _min:
            _min = res
    return _min+1

def egg_drop_puzzle2(n, k):
    dp = [[0 for i in xrange(n+1)] for j in xrange(k+1)]

    for i in xrange(n):
        dp[0][i] = 0
        dp[1][i] = 1

    for i in xrange(k):
        dp[i][1] = i

    for i in xrange(2,k+1):
        for j in xrange(2, n+1):
            dp[i][j] = 10**10

            for _k in xrange(1, i+1):
                res = 1 + max(dp[_k-1][j-1], dp[i -_k][j])
                if res < dp[i][j]:
                    dp[i][j] = res

    for a in dp:
        print a 
    return dp[k][n]
print egg_drop_puzzle2(2, 10)

print egg_drop_puzzle(2, 10)
