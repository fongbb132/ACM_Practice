def floyd_warshall(map):
    if not map or len(map[0]) == 0 :
        return 0

    l = len(map)

    dp = [[i for i in b] for b in map]
   
    for i in xrange(l):
        for j in xrange(l):
            for k in xrange(l):
                dp[j][k] = min(dp[j][k], dp[j][i] + dp[i][k])
    return dp

map = [[0, 5, 10**10, 10],[10**10, 0,  3, 10**10],[10**10, 10**10, 0, 1],[10**10, 10**10, 10**10, 0]]
map2 = [[0, 4, 6, 1],[10**10, 0, 2, 3],[10**10, 10**10, 0, 10**10],[10**10, 1, 4, 0]]
# result = floyd_warshall(map)
result2 = floyd_warshall(map2)
for a in result2:
    print a
