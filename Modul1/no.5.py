##no.5
print("=======Nomer 5======")
from math import sqrt as sq
def prima(n):
    n = int(n)
    assert n>=0
    primakcl = [2,3,5,7,11]
    bukanprima = [0,1,4,6,8,9,10]
    if n in primakcl:
        return True
    elif n in bukanprima:
        return False
    else :
        for i in range(2,int(sq(n))+1):
            if (n % i) == 0:
                print(n, "bukan bilangan prima")
                break
        else:
            print(n,"adalah bilangan prima")
print (prima(17))
