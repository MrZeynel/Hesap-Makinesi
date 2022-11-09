print("""

Hesap Makinesi

Toplama: 1
Çıkarma: 2
Çarpma: 3
Bölme: 4

Lütfen yapmak istediğiniz işlemi seçmek için sayı seçin.

""")

islem = str(input("İşlem Seçiniz: "))

if islem == "1":
   sayi1 = int(input("Birincil Sayı: "))
   sayi2 = int(input("İkincil Sayı: "))
   print ("Sonuç = ", sayi1 + sayi2)

if islem == "2":
   sayi1 = int(input("Birincil Sayı: "))
   sayi2 = int(input("İkincil Sayı: "))
   print ("Sonuç = ", sayi1 - sayi2)

if islem == "3":
 sayi1 = int(input("Birincil Sayı: "))
sayi2 = int(input("İkincil Sayı: "))
print ("Sonuç = ", sayi1 * sayi2)

if islem == "4":
 sayi1 = int(input("Birincil Sayı: "))
sayi2 = int(input("İkincil Sayı: "))
print ("Sonuç = ", sayi1 / sayi2)
