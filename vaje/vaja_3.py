"""
def resultat_igre():
    domači = int(input("Domači: "))
    gosti = int(input("Gosti: "))
    print(f"popravljen rezultat: {domači}:{gosti}")
    print(f"Skupni resultat: {domači + gosti}")

resultat_igre()
"""
"""
def čas_igre():
    zaloga_minuta = int(input("Minute igranja: "))
    minuta = zaloga_minuta % 60
    zura = zaloga_minuta // 60
    ura = zura % 24
    dan = zura // 24
    print(f"igrali ste {dan} dni, {ura} ur, {minuta} minut")

čas_igre()
"""

import math
def pizza_za_razred():
    dijaki = 25
    pizza = 9
    cena_pizze = 9.50
    pizza = math.ceil(pizza)
    skupna_cena = cena_pizze * pizza
    print(f"skupna cena: {skupna_cena}€")
    print(f"cena na dijaka: {skupna_cena / dijaki}€")

#pizza_za_razred()

def kino_cena():
    starost = int(input("Starost: "))
    #dan = str(input("Dan: "))
    if starost < 6:
        cena = 0
    elif starost < 18:
        cena = 5
    elif starost < 65:
        cena = 8
    else:
        cena = 6



kino_cena()
