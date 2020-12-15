def EEA(a, b):
  (Xa, Ya) = (1, 0)
  (Xb, Yb) = (0, 1)
  while(a%b):
    q = int(a/b)
    r = a%b
    a = b
    b = r
    Xr = Xa - q*Xb
    Yr = Ya - q*Yb
    (Xa, Ya) = (Xb, Yb)
    (Xb, Yb) = (Xr, Yr)
  return (Xb, Yb)

a = int(input('nhập số a: '))
b = int(input('nhập số b: '))
(resX,resY) = EEA(a,b)
print('result is x = {} and y = {}'.format(resX, resY))