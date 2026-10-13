"""
import requests

url = "https://api.frankfurter.dev/v1/latest"
odgovor = requests.get(url, params={"symbols": "USD,GBP,CHF,JPY"})

if odgovor.status_code != 200:
    print("Napaka pri klicu API-ja.")
    exit()

podatki = odgovor.json()
tecaji = podatki["rates"]   

print("Tečaji na dan", podatki["date"])

for valuta, tecaj in tecaji.items():
    print(valuta + ":", tecaj)

print("Skupaj valut:", len(tecaji))
"""
'''
import requests

url = requests.get("https://api.frankfurter.dev/v1/latest").json()
tecaji = url["rates"]


def v_tujo(evri, valuta, tecaji):
    print(evri, valuta, tecaji)
    if valuta not in tecaji:
        return None
    return evri * tecaji[valuta]      # 1 EUR = tečaj, zato množimo


def v_evre(znesek, valuta, tecaji):
    if valuta not in tecaji:
        return None
    return znesek / tecaji[valuta]    # obratna smer, zato delimo


evri = float(input("Znesek v EUR: "))     # input vrne niz, rabimo število
valuta = input("Valuta: ").upper()        # chf -> CHF

tuje = v_tujo(evri, valuta, tecaji)

if tuje is None:
    print("Valuta", valuta, "ne obstaja.")
else:
    print(evri, "EUR =", round(tuje, 2), valuta)
    nazaj = v_evre(tuje, valuta, tecaji)
    print(round(tuje, 2), valuta, "=", round(nazaj, 2), "EUR")
'''
'''
import requests

url = "https://api.frankfurter.dev/v1/2026-09-01..2026-09-07"
podatki = requests.get(url, params={"symbols": "JPY"}).json()
dnevi = podatki["rates"]          # datum -> {"USD": tečaj}

datumi = list(dnevi.keys())       # seznam, da lahko uporabljamo indekse

# prvi dan nima prejšnjega, zato ga izpišemo posebej
print(datumi[0] + ":", dnevi[datumi[0]]["JPY"])

for i in range(1, len(datumi)):
    danes = dnevi[datumi[i]]["JPY"]
    vceraj = dnevi[datumi[i - 1]]["JPY"]

    if danes > vceraj:
        smer = "gor"
    else:
        smer = "dol"

    print(datumi[i] + ":", danes, "(" + smer + ")")

print("Podatki od", datumi[0], "do", datumi[-1] + ", skupaj", len(datumi), "dni")
'''
'''
import requests

valute = ["USD", "GBP", "CHF"]

url = "https://api.frankfurter.dev/v1/latest"
podatki = requests.get(url, params={"symbols": ",".join(valute)}).json()
tecaji = podatki["rates"]

for a in valute:              # iz katere valute
    for b in valute:          # v katero valuto
        if a == b:
            continue          # USD -> USD nas ne zanima

        tecaj = tecaji[b] / tecaji[a]   # oba sta glede na EUR, zato ju delimo
        print("1", a, "=", round(tecaj, 4), b)
'''

import requests

url = "https://api.frankfurter.dev/v1/2026-09-01..2026-09-30"
podatki = requests.get(url, params={"symbols": "GBP"}).json()
dnevi = podatki["rates"]

prihranki = 800

# začnemo s prvim dnem, nato primerjamo vse ostale
prvi_dan = list(dnevi.keys())[0]
najboljsi = prvi_dan
najslabsi = prvi_dan
vsota = 0

# 1. zanka: najboljši, najslabši dan in vsota za povprečje
for datum, tecaji_dne in dnevi.items():
    tecaj = tecaji_dne["GBP"]

    if tecaj > dnevi[najboljsi]["GBP"]:
        najboljsi = datum
    if tecaj < dnevi[najslabsi]["GBP"]:
        najslabsi = datum

    vsota = vsota + tecaj

povprecje = vsota / len(dnevi)

# 2. zanka: šele zdaj poznamo povprečje in lahko štejemo
nad = 0
for tecaji_dne in dnevi.values():
    if tecaji_dne["GBP"] > povprecje:
        nad = nad + 1

najvec = prihranki * dnevi[najboljsi]["GBP"]
najmanj = prihranki * dnevi[najslabsi]["GBP"]

print("Najboljši dan:", najboljsi, "->", round(najvec, 2), "GBP")
print("Najslabši dan:", najslabsi, "->", round(najmanj, 2), "GBP")
print("Razlika:", round(najvec - najmanj, 2), "GBP")
print("Povprečni tečaj:", round(povprecje, 4))
print("Dni nad povprečjem:", nad, "od", len(dnevi))
