import random as rand
import math

def factorize (n):
# Output [(p1,e1), (p2, e2), ..., (pr, er)]
# sqrt(n)lg(n) algorithm
    i=2
    ans=[]
    while i*i <= n:
        if n%i==0:
            e=0
            p=i
            while n%i==0:
                e+=1
                n=n//i
            ans.append((p,e))
        i+=1
    if n != 1:
        ans.append((n,1))
    return ans
def norm (a, mod):
    a %= mod
    if a<0:
        a+=mod
    return a
def find_generator (p):
    print("Finding generator")
    qe=factorize(p-1)
    r=len(qe)
    y=1

    for i in range(r):
        q,e = qe[i]
        #print("q_i e_i: ",q," ",e)
        # Try to brute force till a small range?
        found=False
        for a in range(2,math.ceil(math.sqrt(p))):
            b=pow(a,(p-1)//q,p)
            #print("a b: ",a,b)
            if b!=1:
                found=True
                break
        if not found: # Resort to probabilistic
            while True:
                a = rand.randint(2,p-1)
                b = pow(a,(p-1)//q,p)
                if b!=1:
                    break
        q_pow_e = pow(q,e)
        #print("Chosen a: ",a)
        y_i=pow(a,(p-1)//q_pow_e,p)
        y = (y*y_i) % p
    return norm(y,p)
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
def inverse_mod (a, mod):
    d,s,t = extend_euclid(a, mod)
    if d != 1:  # No modular inverse
        return None
    else:
        return norm (s, mod)

def baby_step_giant_step (a, y, p):
    # find log_y(a) modulo p, assume p is odd prime
    # a and y in Z*p

    # Baby step
    # print("Baby step start")
    T = {}
    b=1; m=math.ceil(math.sqrt(p-1))
    for i in range(m):
        T[b]=i
        b=(b*y)%p
    
    # Giant step
    # print("Giant step start")
    yp=inverse_mod(pow(y,m,p),p)
    b=a; j=0
    while b not in T:
        b=(b*yp)%p
        j+=1
        #print("Current b: ",b)
    i=T[b]
    x=j*m+i
    return norm(x,p)

if __name__ == "__main__":
    p=int(input("Enter odd prime p: "))
    y=find_generator(p)
    print("Generator y: ",y)
    a=int(input("Enter a in Z*p: "))
    a=norm(a,p)
    k=baby_step_giant_step(a,y,p)
    print("Log_y(a): ",k)
    print("TEST y^log_y(a): ",pow(y,k,p))
