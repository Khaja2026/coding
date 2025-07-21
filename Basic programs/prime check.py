# Enter your code here
def is_prime(num):
    if num<2:
        return "not a prime num"
    elif num==2:
        return "prime"
    else:
        for i in range(2,num):
            if num%i==0:
                return "not prime"
                break
        else:
            return "prime"
print(is_prime(12))