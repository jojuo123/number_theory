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
def quadratic_residue_list(p):
    ret_list=[]
    for i in range(p):
        tmp = i**2
        tmp = tmp % p
        ret_list.append(tmp)
    ret_list = list(set(ret_list))
    return ret_list

def find_result(p):
    qlist = quadratic_residue_list(p)
    result = 0
    for i in range (0,len(qlist)-1):
        if(qlist[i+1]-qlist[i]>1):
            result = qlist[i] + 1
            return result
    return result

p = int(input("Nhap so hang: "))
if (is_prime(p) and (p - 1) % 4 == 0):
    result = find_result(p) 
    tmp = int((p-1)/4)
    if(tmp < 50): 
        print (result**tmp)
    else:
        print(pow(result, tmp, p))
else:
    print("Invalid input")

    
