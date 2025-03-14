
def carpma(*args):
    sc = 1
    for sayi in args:
        sonuc *= sayi
    return sonuc

def cikarma(*sayilar):
    if not sayilar:
        return 0
    sonuc = sayilar[0]
    for sayi in sayilar[1:]:
        sonuc -= sayi
    return sonuc

def topla(*sayilar):
    return sum(sayilar)

import math

def karekok_al(*args):
    for sayi in args:
        if sayi >= 0:
            print(f"{sayi} sayısının karekökü: {math.sqrt(sayi)}")
        else:
            print(f"{sayi} negatif bir sayı olduğu için karekökü alınamaz.")



