def coin_change(N,  S, holder, result):
    if N == 0:
        # print holder
        result.append(holder)
    if N < 0:
        return []
    for i in S:
        temp =  holder + [i]
        coin_change(N-i, S,  temp, result)
    return result

def coin_change2(coins, target):
    n = len(coins)
    m = target

    dp = [[1 if j == 0 else 1 for i in xrange(n)]for j in xrange(m+1)]

    for i in xrange(1, m+1):
        for j in xrange(n):
            x = dp[i-coins[j]][j] if i - coins[j] >= 0 else 0
            y = dp[i][j-1] if j - 1 >= 0 else 0 
            dp[i][j] = x + y
    return dp[m][n-1]
    

result = coin_change(10, [2,5,3,6], [], [])
print result 
print len(result)

print coin_change2([2,5,3,6], 10)
