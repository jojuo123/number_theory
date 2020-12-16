def jacobi(a, n):
    if n <= 0:
        raise ValueError("'n' must be a positive integer.")
    if n % 2 == 0:
        raise ValueError("'n' must be odd.")
    a %= n
    result = 1
    while a != 0:
        while a % 2 == 0:
            a /= 2
            n_mod_8 = n % 8
            if n_mod_8 in (3, 5):
                result = -result
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            result = -result
        a %= n
    if n == 1:
        return result
    else:
        return 0

def bookJacobi(a, n):
    result = 1
    while True:
        a %= n
        if a == 0:
            if n == 1:
                return result
            else:
                return 0
        h = 0
        a_pr = a
        while a_pr % 2 == 0:
            a_pr //= 2
            h += 1
        if h % 2 == 1 and (n % 8 != 1 and n % 8 != 7):
            result = -result
        if a_pr % 4 != 1 and n % 4 != 1:
            result = -result
        a, n = n, a_pr
if __name__=='__main__':
    a = int(input('enter a: '))
    n = int(input('enter n: '))
    print('jacobi', jacobi(a, n))
    print(bookJacobi(a, n))