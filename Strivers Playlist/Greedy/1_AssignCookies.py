def AssignCookies(a,b):
    ''' where a is the greed
    and b is the cookies to be assigned '''
    a.sort()
    b.sort()
    n,m = len(a), len(b)
    l, r = 0,0
    while l<n and r<m:
        if(b[r]>=a[l]):
            l+=1
        r+=1
        
    return l

a = [1, 2, 3]
b = [1, 1]
print(AssignCookies(a, b))  # Output: 1 