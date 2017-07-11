def edit_distance(s1, s2):
    if not s1:
        return len(s2)

    if not s2:
        return len(s1)

    if s1[-1] == s2[-1]:
        return edit_distance(s1[:-1], s2[:-1])

    return 1+ min(min(edit_distance(s1[:-1], s2), \
                  edit_distance(s1, s2[:-1])),\
                  edit_distance(s1[:-1], s2[:-1]))

def edit_distance2(s1, s2):
    n1 = len(s1)
    n2 = len(s2)

    dp = [[0]*(n1+1)for i in range(n2+1)]
    # for a in dp:
    #     print a
    for i in xrange(n2+1):
        for j in xrange(n1+1):
            if i == 0:
                # print i,  j, j 
                dp[i][j] = j

            elif j == 0:
                dp[i][j] = i

            elif(s1[j-1]==s2[i-1]): dp[i][j] = dp[i-1][j-1]

            else: dp[i][j] = 1 + min(min(dp[i][j-1], dp[i-1][j]),
                                     dp[i-1][j-1])

            print i, j
            
            for  a in dp:
                print a
    return dp[n2][n1]
            
print edit_distance("saturday", "sunday")
print edit_distance2("saturday", "sunday")

# print edit_distance2("Hellofdasfasdfsavn", "fsdaflknchelkjfsadlo") 
