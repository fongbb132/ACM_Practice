def min_cost_path(map):
    if not map: return 0
    w = len(map)
    h = len(map[0])

    dp = [[0] * (w+1) for i in xrange(h+1) ]

    for i in xrange(1, h+1):
        for j in xrange(1, w+1):
            dp[i][j] = min(dp[i-1][j],  dp[i][j-1])+map[i-1][j-1]

    print dp[w][h]

min_cost_path([[1,2,3],[4,8,2],[1,5,3]])