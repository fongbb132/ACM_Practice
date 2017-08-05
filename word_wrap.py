"""
M is the max num of characters can be in 1 line

"""
def word_wrap(lengths, M):
    inf = 10**10
    l = len(lengths)
    spaces = [[for a in xrange(l)]for b in xrange(l)]
    penalties =  [[for a in xrange(l)]for b in xrange(l)]
 
    for i in xrange(1, l+1):
        spaces[i][i] = M - lengths[i] 
        for j in xrange(i, l+1):
            spaces[i][j] = spaces[i][j-1] - lengths[j] - 1
    
    for i in xrange(1, l+1):
        for j in xrange(i, l+1):
            if spaces[i][j] < 0 :
                penalties[i][j] = inf
            elif j == l and spaces[i][j] >= 0: 
                penalties[i][j] = 0
            else:
                penalties[i][j] = spaces[i][j]**2
    cost = [for i in xrange(l)]
    for i in xrange(1, l+1):
        cost[i] = inf 
        for j in xrange(i, l+1):
            if cost[i-1] != inf and penalties[i][j] != inf:
                cost[j] = min(cost[i-1] + penalities[i][j])
  
                
