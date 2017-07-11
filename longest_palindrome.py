def longestPalindrome(s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n == 0 :
            return ""
        
        dp = [[1 if j == i else 0 for i  in xrange(n)]for j in xrange(n) ]
        _max = 0
        result = s[0]
        
        for i in xrange(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 1 
                result = s[i: i+2]
        
        
        for i in xrange(3,  n+1, 1):
            for j in xrange(0,  n-i+1, 1):
                if s[j] == s[j+i-1] and dp[j+1][j+i-2]:
                    _max = max(_max, i)
                    dp[j][j+i-1] = 1
                    result = s[j:j+i]
        for i in dp: print i                    
        return result

def longestPalindrome_2(s):
    """
    :type s: str
    :rtype: str
    O(n)
    """
    n = len(s)
    if n == 0 :
        return ""
    max_len, start = 1, 0
    
    for i in xrange(n):
        if i - max_len >= 1 and s[i-max_len-1:i+1]==s[i-max_len-1:i+1][::-1]:
            start = i - max_len -1
            max_len += 2
        elif i - max_len >= 0 and s[i-max_len: i+1] ==s[i-max_len: i+1][::-1]:
            start = i - max_len 
            max_len += 1
            
    return s[start: max_len+start]
print longestPalindrome_2("ABCBA")
