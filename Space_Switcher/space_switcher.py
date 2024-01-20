import os

dosya_adi = input("NOT: BU UYGULAMAYI KULLANMADAN ONCE DOSYANIZI YEDEKLEYINIZ!!!\nBosluklarin tablarla değiştirileceği dosya ismini giriniz: \n")

dosyaoku = open(dosya_adi + ".txt", "r")

dosyasatirlari = dosyaoku.readlines()

dosyaoku.close()
yeni_dosya_satirlari = []
for satir in dosyasatirlari:
	yenisatir = ""
	for sayaç in range(0, len(satir), 4):
		try:
			if satir[sayaç:sayaç+4] == "    ":
				yenisatir = yenisatir + "\t"
			else:
				yenisatir = yenisatir + satir[sayaç:sayaç+4]
		except:
			yenisatir = yenisatir + satir[sayaç:]
	yeni_dosya_satirlari.append(yenisatir)

print(yeni_dosya_satirlari)

yepyenidosya = open(dosya_adi + "_edited.txt", "w")

for satir in yeni_dosya_satirlari:
	yepyenidosya.write(satir)

yepyenidosya.close()
#print(dosyasatirlari)


