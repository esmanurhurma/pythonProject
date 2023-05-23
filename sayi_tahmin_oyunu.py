#1-100 arası rastgele üretilen sayıyı aşağı yukarı ifadeleri ile
#buldurmaya çalışma (hak=5)
#100 üzerinden puanlama yapılıyor. Her soru 20 puan.

import random

sayi=random.randint(1,100)
hak=5
sayac=0

while hak >0:
    hak -=1
    sayac +=1
    tahmin =int(input("tahmin: "))

    if sayi == tahmin:
        print(f"tebrikler {sayac}. defada bildiniz. Toplam puanınız: {100 -(20)*(sayac-1)}")
        break
    elif sayi > tahmin :
        print("yukarı")
    else:
        print("aşağı")

    if hak ==0:
        print(f"hakkınız bitti. Tutulan sayı : {sayi}")