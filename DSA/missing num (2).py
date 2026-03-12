arr=list(map(int,input().split()))
n=len(arr)
total=n*(n+1)//2
print(total-sum(arr))