def rev(n):
    s=len(str(n))
    rev=0
    for i in range(s):
        rev=rev*10+n%10
        n=n//10
    return rev
print(rev(1234))
        
    