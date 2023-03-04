print ("""
Hesaplama makinesi

Lütfen işleminizi seçiniz:

1 Toplama
2 Çıkarma
3 Çarpma
4 Bölme
F Çıkış
""")

while True:

    islem = str(input("İşlem Seçiniz:"))

    if islem == "1":
     sayi1 = int(input("Birincil Sayı: "))
     sayi2 = int(input("İkincil Sayı: "))
     print ("\n\nSonuç: ", sayi1 + sayi2)

    elif islem == "2":
        sayi1 = int(input("Birincil Sayı: "))
        sayi2 = int(input(" İkincil Sayı: "))
        print ("\n\nSonuç: ", sayi1 - sayi2)

    elif islem == "3":
        sayi1 = int(input("Birincil Sayı: "))
        sayi2 = int(input(" İkincil Sayı: "))
        print ("\n\nSonuç: ", sayi1 * sayi2)

    elif islem == "4":
        sayi1 = int(input("Birincil Sayı: "))
        sayi2 = int(input(" İkincil Sayı: "))
        print ("\n\nSonuç: ", sayi1 / sayi2)

    elif islem == "F":
         break

    else:
     print("Yanlış seçenek!")