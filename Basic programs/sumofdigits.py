def sum_of_digits(n):
    s=len(str(n))
    sum=0
    for i in range(s):
        digit=n%10
        sum+=digit
        n=n//10
    return sum
print(sum_of_digits(1234))
        
    