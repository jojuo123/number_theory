import copy
from functools import reduce
import math

def power(base, exp, modulus):
    result = 1
    base = base % modulus
    while (exp > 0):
        if (exp % 2 == 1):
            result = (result * base) % modulus
        exp = int(exp) >> 1
        base = (base * base) % modulus
    return result % modulus

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def order(p, b):
    if gcd(p, b) != 1:
        return -1
    
    k = 3
    while True:
        if power(b, k, p) == 1:
            return k
        k += 1

def modular_sqrt(a, p):

    def legendre_symbol(a, p):
        ls = pow(a, (p - 1) // 2, p)
        return -1 if ls == p - 1 else ls

    if legendre_symbol(a, p) != 1:
        return -1
    elif a == 0:
        return 0
    elif p == 2:
        return p
    elif p % 4 == 3:
        return pow(a, (p + 1) // 4, p)

    s = p - 1
    e = 0
    while s % 2 == 0:
        s //= 2
        e += 1

    n = 2
    while legendre_symbol(n, p) != -1:
        n += 1

    x = pow(a, (s + 1) // 2, p)
    b = pow(a, s, p)
    g = pow(n, s, p)
    r = e

    while True:
        t = b
        m = 0
        for m in range(r):
            if t == 1:
                break
            t = pow(t, 2, p)

        if m == 0:
            return x

        gs = pow(g, 2 ** (r - m - 1), p)
        g = (gs * gs) % p
        x = (x * gs) % p
        b = (b * g) % p
        r = m

def PrimeModSqrt(a, p):
    x = modular_sqrt(a, p)
    return x if x <= (p - 1) / 2 else (p - x)

def gcdExtended(a, b):  
    if a == 0 :   
        return b,0,1
             
    gcd,x1,y1 = gcdExtended(b%a, a)  

    x = y1 - (b//a) * x1  
    y = x1  
     
    return gcd,x,y

def ModInv(a, n):
    d, x, y = gcdExtended(a, n)
    return (x % n + n) % n

def findsol(a, b, n):
    d = gcd(a, n)
    if b % d != 0:
        return None
    a = a / d
    b = b / d
    n = n / d
    t = ModInv(a, n)
    z = (t * b) % n
    return z
    
def HenselLifting(a, p, exp):
    dp = [0 for i in range(exp + 1)]
    dp[1] = PrimeModSqrt(a, p)
    if (dp[1] == -1):
        print('No solution')
        return -1
    i = 2
    ppf = 1
    while i <= exp:
        b = dp[i - 1] #b^2 = a (mod p^f)
        b2 = b * 2
        c = a - b*b
        ppf *= p #p^f
        c = c // ppf
        while c < 0:
            c += p
        while c >= p:
            c -= p
        h = findsol(b2, c, p)
        if h is None:
            print('No solution')
            return -1
        dp[i] = (ppf*h + b) % (ppf * p)
        i += 1
    return copy.deepcopy(int(dp[exp]))
    
def Sieve(n):
    isPrimes = [True for i in range(n+1)]
    isPrimes[0] = isPrimes[1] = False
    global primes
    for i in range(2, n + 1):
        if isPrimes[i]:
            j = i * i
            while j <= n:
                isPrimes[j] = False
                j += i
            primes.append(i)
    return primes

def Factorize(n):
    factors = []
    global primes
    pf_idx = 0
    if len(factors) == 0:
        factors.append([n, 1])
    return factors
    pf = primes[pf_idx]
    while (pf * pf <= n):
        cnt = 0
        while n % pf == 0:
            n /= pf
            cnt += 1
        if cnt > 0:
            factors.append([pf, cnt])
        pf_idx += 1
        pf = primes[pf_idx]
    if n != 1:
        factors.append([n, 1])
    return factors

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * ModInv(p, n_i) * p
    return sum % prod

def CompositeModularSqrt(a, n):
    global primes
    Sieve(math.ceil(math.sqrt(n)))
    if n % 2 == 0:
        print('No solution')
        return -1
    factors = Factorize(n)
    nCRT = []
    aCRT = []
    for f in factors:
        a_i = HenselLifting(a, f[0], f[1])
        if a_i == -1:
            print('No solution')
            return 0
        n_i = f[0]**f[1]
        nCRT.append(n_i)
        aCRT.append(a_i)
    return int(chinese_remainder(nCRT, aCRT))

primes = []
if __name__=='__main__':
    
    a = int(input('enter a: '))
    n = int(input('enter n: '))
    print('SQRT: ', CompositeModularSqrt(a, n))
    #print(power(287, 2, 673))
    #print(HenselLifting(3, 2003, 1))