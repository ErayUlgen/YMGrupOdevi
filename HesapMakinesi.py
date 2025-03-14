print("Merhaba Dünya")
def cikarma(*sayilar):
    if not sayilar:
        return 0
    sonuc = sayilar[0]
    for sayi in sayilar[1:]:
        sonuc -= sayi
    return sonuc

