##no.7
print("=======Nomer 7======")
def faktorprima(x):
    a=[]
    b=2
    while b<=x:
        if x%b==0:
            x/=b
            a.append(b)
        else:
            b+=1
    print(a)
    
faktorprima(120)
