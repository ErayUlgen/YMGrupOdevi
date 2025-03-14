def carpma(*args):
    if len(args) == 0:
        return 0
    sonuc = 1
    for sayi in args:
        sonuc *= sayi
    return sonuc

sayi_listesi = input("Carpilacak sayilari aralarina bosluk koyarak girin : ").split()

if len(sayi_listesi) == 0 or not sayi_listesi[0]:
    print("Sonuc: 0")
else:
    sayilar = [float(sayi) for sayi in sayi_listesi]
    print(f"Sonuc: {carpma(*sayilar)}")
