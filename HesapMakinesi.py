
import math

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


def bolme(*sayilar):
    sonuc = sayilar[0]
    for i in sayilar[1:]:
        try:
            sonuc=sonuc/i
        except ZeroDivisionError:
            print("SIFIRA BOLME HATASI")
            return
    return sonuc
            

def karekok_al(sayi):
    return math.sqrt(sayi)

def mod_al(a, b):
    return a % b



