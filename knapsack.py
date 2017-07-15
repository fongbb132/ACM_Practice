def knapsack(W, wt, val):
    if len(wt) == 0 or W == 0 :
        return 0
    if wt[0]>W:
        return knapsack(W, wt[1:], val[1:])
    else:
        return max(knapsack(W, wt[1:], val[1:]), (val[0] + knapsack(W-wt[0], wt[1:], val[1:])))

def knapsack2(W, wt, val):
    v = len(val)+1
    
    dp = [[0 for a in xrange(v)]for b in xrange(W+1)]

    for w in xrange(W+1):
        for j in xrange(v):
            if w == 0 or j == 0:
                dp[w][j] = 0 
            # elif w >= wt[j-1]:
            #     dp[w][j] = max(val[j-1] + dp[w-wt[j-1]][j-1], dp[w][j-1])
            elif w<wt[j-1]:
                dp[w][j] = dp[w][j-1]
            else:
                dp[w][j] = max(val[j-1] + dp[w-wt[j-1]][j-1], dp[w][j-1])
            
    return dp[W][v-1]
print knapsack(50, [10, 20, 30], [60, 100, 120])

print knapsack2(50, [10, 20, 30], [60, 100, 120])