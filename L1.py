import math
def is_prime(n: int) -> bool:
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def __findAllprime(p):
    ###find all prime smaller than square root of p
    list = []
    r =  int(math.sqrt(p))
    for i in range (2,r+1):
        if(is_prime(i)):
            list.append(i)
    return list
def __Factorization(p):
    list = []
    if(is_prime(p) == False):
        prime = __findAllprime(p)
        i = 0
        while(p != 1 and i < len(prime)):
            if p % prime[i] == 0:
                list.append(prime[i])
                while(p % prime[i] == 0):
                    p = p / prime[i]
            i+=1
    else:
        list.append(p-1)
    return list
def __phi(p):
    prime = __Factorization(p)
    phi_p = p
    for i in range(len(prime)):
        phi_p = phi_p * (1 - 1/prime[i])
    return int(phi_p)

def __calculate_remainder(p, exponent, divided):
    p = p % divided
    exponent = exponent % __phi(divided)
    result = p ** exponent
    result = result % divided
    return result

p = int(input("Nhap so hang: "))
exponent = int(input("Nhap so mu: "))
divided = int(input("Nhap so chia: "))

result = __calculate_remainder(p,exponent, divided)
print("Result:",result)


