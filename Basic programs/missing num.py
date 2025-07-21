def missing(a):
    org_sum=0
    cal_sum=0
    n=len(a)
    for i in range(0,n):
        cal_sum=cal_sum+a[i]
    org_sum=n*(n+1)//2
    return org_sum - cal_sum

a=list(map(int,input().split()))

print(missing(a))