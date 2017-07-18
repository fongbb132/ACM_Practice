"""
    i + j = m - i + n - j (or m-i + n - j + 1) 
    2j = m - 2i + n 
    j = (m+n)/2 - i (or (m+n+1)/2 - i) 


"""

def median(A, B):
    l1, l2 = len(A), len(B)

    # make sure that A is always larger than B
    if l1 < l2:
        A, B, l1, l2 = B, A, l2, l1

    imin, imax, half_len = 0, l2, (l1+l2+1)/2

    while imin <= imax:
        i = imin + (imax - imin)/2
        j = half_len - i 

        if i < l2 and B[i] < A[j-1]:
            imin = i + 1
        elif i > 0 and B[i-1] > A[j]:
            imax = i - 1
        else:
            # max_of_left because the case of B[i-1] > A[j] would not happen, A[j-1] >= B[i] is the only situation
            if i == 0:max_of_left = A[j-1]
            elif j == 0: max_of_left = B[i-1]
            else:
                max_of_left = max(A[j-1], B[i-1])
            if (m+n)%2 == 1:
                return max_of_left

            if i == l2: min_of_right = A[j]
            elif j == l1: min_of_right = B[i]
            else: min_of_right = min(A[j], B[i])

            return (max_of_left+min_of_right)/2.0





    
