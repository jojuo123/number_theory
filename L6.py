def RSA(base: int, exp: int):
    res = 1
    i = int(exp)
    while i > 0:
        if(i % 2 != 0):
            res = res*base
        base = base*base
        i = int(i/2)
    return res
def EEAstep(r, s, t, rr, ss ,tt):
    try:
        q = int(r/rr)
    except ZeroDivisionError:
        return r, s, t, rr, ss, tt, False
    rrr= r%rr
    return rr, ss, tt, rrr, s-ss*q, t-tt*q, True
def inspectDecimal(n: float):
    string = str(n)
    tmp = string[::-1].find('.')
    k = int(tmp)
    tmp_arr = string.split(".")
    ipart = int(tmp_arr[0])
    dpart = int(tmp_arr[1])
    return ipart,dpart,k
def reconstructRNSolOnly(n: float, ub: int):#assume the decimal number is long, > 5 digits to be safely run
    ipart, dpart, k = inspectDecimal(n)
    m = RSA(10,k)
    r,s,t,rr,ss,tt, check = EEAstep(m,1,0,dpart,0,1)
    bs = s
    bt = t
    while tt<ub and check:
        bss = ss
        btt = tt
        r,s,t,rr,ss,tt, check = EEAstep(r,s,t,rr,ss,tt)
    return abs(bss), abs(btt)
def reconstructRNFullSol(n: float, ub: int):#assume the decimal number is long, > 5 digits to be safely run
    ipart, dpart, k = inspectDecimal(n)
    m = RSA(10,k)
    line = []
    res_arr = []
    res_arr.append(["step","r","s","t","r'","s'","t'"])
    res_arr.append([0,m,1,0,dpart,0,1])
    r, s, t, rr, ss, tt, check = EEAstep(m,1,0,dpart,0,1)
    line.append(1)
    line.append(r)
    line.append(s)
    line.append(t)
    line.append(rr)
    line.append(ss)
    line.append(tt)
    res_arr.append(line)
    i = 2
    while abs(tt)<ub and check:
        line = []
        r, s, t, rr, ss, tt, check = EEAstep(r, s, t, rr, ss, tt)
        line.append(i)
        line.append(r)
        line.append(s)
        line.append(t)
        line.append(rr)
        line.append(ss)
        line.append(tt)
        res_arr.append(line)
        i+=1
    return res_arr
def printSolOnly(n:float, ub:int):
    a,b = reconstructRNSolOnly(n,ub)
    print(a,end="")
    print("/",end="")
    print(b)
def printFullSol(n:float, ub: int):
    ipart, dpart, k = inspectDecimal(n)
    print("Perform EEA on 10^",end = "")
    print(k,"and", dpart)
    res_arr = reconstructRNFullSol(n,ub)
    for line in res_arr:
        print('{:>10} {:>10} {:>10} {:>10} {:>10} {:>10} {:>10}'.format(*line))
    print("(s, t) in the line just above final line is the solution:", end=" ")
    print(abs(res_arr[len(res_arr)-2][5]),end = "")
    print("/",end="")
    print(abs(res_arr[len(res_arr)-2][6]))
#test lab 2019
if __name__ == "__main__":
    test_case = [0.372636, 0.373346671, 0.2173836482, 0.09375] #0.09365 is an extra to ensure
    precision = [1000, 10000, 100000, 100]
    i = 1
    j = 0 #set j = 1 for detailed solution
    for t in test_case:
        print("test:",i)
        if j:
            printFullSol(t,precision[i-1])
        else:
            printSolOnly(t,precision[i-1])
        i+=1
        print()
        

