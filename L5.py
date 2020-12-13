def isPrime(a):
    i = 2
    while i*i <= a:
        if a%i == 0:
            return False
        i+=1
    return True
def EEA(a, b):#unused for Ex05
    r = int(a)
    rr= int(b)
    s = 1
    ss= 0
    t = 0
    tt= 1
    while rr > 0:
        q = int(r/rr)
        rrr= r%rr
        (r,s,t,rr,ss,tt) = (rr, ss, tt,rrr,s-ss*q,t-tt*q)
    d = r
    return d,s,t
def EEAstep(r, s, t, rr, ss ,tt):
    q = int(r/rr)
    rrr= r%rr
    return rr, ss, tt, rrr, s-ss*q, t-tt*q
def printEEA():
    print("a =", end = " ")
    a = input()
    print("b =", end = " ")
    b = input()
    d,s,t = EEA(a,b)
    print("gcd = ", d, "; s = ", s,"; t =", t)
    print("check: ", a,"*",s," + ",b,"*",t," = ",d)
def RSA(base: int, exp: int, mod: int):
    res = 1
    i = int(exp)
    while i > 0:
        if(i % 2 != 0):
            res = (res*base)%mod
        base = (base*base)%mod
        i = int(i/2)
    return res
def findBeta(p: int): #assume p is prime
    for i in range(2,p):
        if RSA(i,(p-1)/2,p) == p-1:
            return RSA(i,(p-1)/4, p)
def F2SAFullSol(p: int): # return detailed solution
    b = findBeta(p)
    if not b:
        return []
    line = []
    res_arr = []
    res_arr.append(["step","r","s","t","r'","s'","t'"])
    res_arr.append([0,p,1,0,b,0,1])
    r, s, t, rr, ss, tt = EEAstep(p,1,0,b,0,1)
    line.append(1)
    line.append(r)
    line.append(s)
    line.append(t)
    line.append(rr)
    line.append(ss)
    line.append(tt)
    res_arr.append(line)
    i = 2
    while r*r > p:
        line = []
        r, s, t, rr, ss, tt = EEAstep(r, s, t, rr, ss, tt)
        line.append(i)
        line.append(r)
        line.append(s)
        line.append(t)
        line.append(rr)
        line.append(ss)
        line.append(tt)
        res_arr.append(line)
        i+=1
    if r*r + t*t != p:
        return []
    return res_arr
def printFullSol(res_arr: list, p):
    if not res_arr:
        print("Something's wrong in the algorithm!")
        return 
    print(">Run repeated squaring agorithm to find beta")
    print("Choose b =",end=" ")
    print(res_arr[1][4], "because", res_arr[1][4], end ="")
    print("^2 = -1 ( mod",p, ")")
    print(">Run Extended Euclidean algorithm to find a,b such that a^2 + b^2 =",p)
    for line in res_arr:
        print('{:>10} {:>10} {:>10} {:>10} {:>10} {:>10} {:>10}'.format(*line))
    print("(r, t) in the final line is the solution:", end=" ")
    print(res_arr[len(res_arr)-1][1],"^2 + ",res_arr[len(res_arr)-1][3],"^2 = ", p, sep="")
def F2SASolOnly(p: int): # only return the result
    b = findBeta(p)
    if not b:
        return False, 0, 0
    r, s, t, rr, ss, tt = EEAstep(p,1,0,b,0,1)
    while r*r > p:
        r, s, t, rr, ss, tt = EEAstep(r, s, t, rr, ss, tt)
    if r*r + t*t != p:
        return False, 0, 0
    return True, r,t
#Test lab 2019
if __name__ == "__main__":
    test_case = [2017, 146837, 252497801, 69] #69 is added to check if the insert number not a prime
    i = 1
    j = 1 #set j to 1 for detailed solution
    if j:
        for p in test_case:
            print("test:",i)
            res_arr = F2SAFullSol(p)
            printFullSol(res_arr, p)
            print()
            i += 1
    else:
        for p in test_case:
            print("test:",i)
            check,a,b = F2SASolOnly(p)
            if check:
                print(a,",",b)
            else:
                print("No solution")
            i+=1