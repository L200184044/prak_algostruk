##no.14
print("=======Nomer 14======")
def frmtRupiah(x):
    a=str(x)
    b=""
    i = -1
    while i>= -len(a):
        if((i+1)%3==0 and (i+1)!=0):
            b="."+b
        b=a[i]+b
        i-=1
    return "Rp "+b
print(frmtRupiah(3400))
