#Trafiğe çıkış tarihi alınan bir aracın servis zamanını verilen bilgilere göre hesaplama
#1.Bakım >> 1.yıl
#2.Bakım >> 2.yıl
#3.Bakım >> 3.yıl
#Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplama
#datetime modülü kulllanalım.

import datetime

tarih = input("aracınız hangi tarihte trafiğe çıktı: ")
tarih = tarih.split('/')
#print(tarih[0])
#print(tarih[1])
#print(tarih[2])

trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi = datetime.datetime.now()
fark =simdi-trafigeCikis
days = fark.days


if days<=365:
    print("1.servis aralığı")
elif days>365 and days<=365*2:
    print("2.servis aralığı")
elif days>365*2 and days<=365*3:
    print("3.servis aralığı")
else:
    print("hatalı süre")