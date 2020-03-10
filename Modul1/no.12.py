##no.12
print("=======Nomer 12======")
from random import*

x = randint(1, 100)
print("saya menyimpan sebuah angka bulat antara 1 sampai 100. Coba tebak")
while True :
    a=int(input("masukan tebakan:>"))
    if a<x:
        print("angka terlalu kecil. Coba lagi")
    elif a>x:
        print("angka terlalu besar. Coba lagi")
    else :
        print("waow! anda benar")
        break
