import math 


def __gcd(a,b):
  if (a%b):
    return __gcd(b,a%b)
  return b

a = int(input('nhập số a: '))
b = int(input('nhập số b: '))
print('(a, b) =', __gcd(a,b))