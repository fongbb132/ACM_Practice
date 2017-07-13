def matrix_chain_order(dimension):
    if not dimension: return 0 

    n = len(dimension)  # n is 1 more than the matrices in the matrix multiplication
    dp =[[0 for x in range(n)]for j in range(n)]

    for i in xrange(2, n):    # length of multiplying sequence
        for j in xrange(1, n - i + 1 ): # check all the sequences with length i 
            end = j + i - 1
            dp[j][end] = 10**10
            for k in xrange(j, end):  # calculate how much it takes to finish the calculation
                temp = dp[j][k] + dp[k+1][end] + dimension[j-1]* dimension[k] * dimension[end]
                dp[j][end] = min(dp[j][end], temp)

    return dp[1][n-1]
            
print matrix_chain_order([40, 20, 30, 10, 30])            
    
    

    
