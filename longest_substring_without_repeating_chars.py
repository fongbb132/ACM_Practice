import collections

def LNRS(s):
    map = collections.defaultdict(lambda:-1)
    if not s: return 0 
    cur = 0
    result = 0
    for i in xrange(len(s)):
        # print map[s[i]]
        result = max(result, min(i - map[s[i]], i-cur))
        if map[s[i]] > -1: cur = map[s[i]]
        map[s[i]] = i
        print s[i], cur, result
    
    return result

print LNRS("geeksforgeeks")