import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if (n%i)==0:
            return False
    return True

def express(n,m):
    s=math.sqrt((2*n-m)/(2*n+m))
    p=m/4*s
    if (p==int(p)) and (is_prime(p)):
        return p
    else:
        return 0

def check_range(r):
    for n in range(1,r+1):
        for m in range(1,2*n):
            p=express(n,m)
            if p!=0:
                print("m:",m,"n:",n,"p:",p)
