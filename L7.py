
#PDF pg 97 / Book pg 79
def extend_euclid (a: int, b: int):
    if (a < b):
        a,b = b,a
        rv=True
    else:
        rv=False
    r=a; rp=b
    s=1; sp=0
    t=0; tp=1
    while rp != 0:
        q=r//rp; rpp=r % rp
        r,s,t,rp,sp,tp = rp,sp,tp,rpp,s-sp*q,t-tp*q
    d=r
    if rv==False:
        return d,s,t
    else:
        a,b=b,a
        return d,t,s
def norm (a, mod):
    a %= mod
    if a<0:
        a+=mod
    return a
def inverse_mod (a, mod):
    d,s,t = extend_euclid(a, mod)
    if d != 1:  # No modular inverse
        return None
    else:
        return norm (s, mod)
def chinese_remainder (a:list, m:list):
    M=1; k=len(a)
    for _m in m:
        M *= _m
    res = 0
    for i in range(k):
        mi_star = M//m[i]
        t_i = inverse_mod(mi_star, m[i])
        e_i = mi_star * t_i
        res += a[i] * e_i
    res %= M
    return res, M

m=[]
a=[]
if __name__ == "__main__":
    print ("CRT x = a_i mod m_i for i=1,...,k. m_i's should be pairwise coprime.")
    print ("Enter two number a_i and m_i at a time")
    print ("Enter two zeroes to stop and print result")
    extend_euclid(3,5)
    while True:
        _a, _m = list(map(int,input("Enter a, m: ").split()))
        if _m==0:
            break
        a.append(_a); m.append(_m)
    k=len(m)
    if k > 0:
        res, M = chinese_remainder(a, m)
        print ("Smallest result: ",res)
        print ("Modulo: ", M)
