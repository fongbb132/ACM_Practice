"""
price is an array of price with the length = (index+1) and the correspoding price is the value in the array
n is the length of rod 
"""
def cut_a_rod(price, n):
    if n <= 0: 
        return 0 
    result = 0 
    for i in xrange(n):
        result = max(result, price[i] + cut_a_rod(price, n - i - 1))
    return result


def cut_a_rod2(price, n):
    if n <= 0 :
        return 0 

    dp = [0 for x in xrange(n+1)]
    for i in xrange(1,n+1):
        m = 0
        for j in xrange(0, i):
            m = max(m, dp[i-j-1]+price[j])
        dp[i] = m
    return dp[n]
print cut_a_rod([1, 5, 8, 9, 10, 17, 17, 20], 8) 
print cut_a_rod2([1, 5, 8, 9, 10, 17, 17, 20], 8) 
