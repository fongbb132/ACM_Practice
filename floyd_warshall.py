def floyd_warshall(map):
    if not map or len(map[0]) == 0 :
        return 0

    l = len(map)

    dp = [[i for i in b] for b in map]
   
    for i in xrange(l):
        for j in xrange(l):
            for k in xrange(l):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    return dp

map = [[0, 5, 10**10, 10],[10**10, 0,  3, 10**10],[10**10, 10**10, 0, 1],[10**10, 10**10, 10**10, 0]]

result = floyd_warshall(map)
for a in result:
    print a
