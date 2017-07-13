"""
C(n, k) = n!/((n-k)!*k!) = (n* (n-1) * ... (n-k+1)) / (k*(k-1)*...*1)
"""
def binomial_coefficient(n, k):
    if n < 1: return 0 
    if n == 1: return 1
    result = 1

    if(k > n-k): k = n - k 


    for i in xrange(0,k):
        result *= n - i 
        result /= i + 1

    return result
print binomial_coefficient(10, 2)