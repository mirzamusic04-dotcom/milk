'''
avto = {
    "znamka": "volkswagen",
    "model": "golf II",
    "letnik": "1991"
}

print(avto["znamka"])      # volkswagen
print(avto["model"])  # golf II
print(avto["letnik"]) 

avto["barva"] = "rdeč"

if "barva" in "avto":
    print("avto je:", avto["barva"])
print(avto.get("gume", "ni podatka"))
for kljuc, vrednost in avto.items():
    print(kljuc, ":", vrednost)
'''
"""
sola = {
    "ime": "ŠC Kranj",
    "naslov": {
        "ulica": "Kidričeva cesta 55",
        "posta": 4000,
        "kraj": "Kranj"
    },
    "smeri": ["računalništvo", "elektrotehnika", "mehatronika"]
}

print(sola["naslov"]["kraj"])   # Kranj
print(sola["smeri"][2])         # računalništvo
print(len(sola["smeri"]))       # 3
"""
"""
import requests

url = "https://api.open-meteo.com/v1/forecast"
parametri = {
    "latitude": 500,
    "longitude": 14.046912571977453,
    "current": "temperature_2m,wind_speed_10m"
}

odgovor = requests.get(url, params=parametri)

print(odgovor.status_code)   # 200 pomeni, da je vse v redu
podatki = odgovor.json()     # JSON pretvorimo v slovar
print(podatki)
{
  "latitude": 500,
  "longitude": 14.046912571977453,
  "current_units": {
    "temperature_2m": "°C",
    "wind_speed_10m": "km/h"
  },
  "current": {
    "time": "2026-10-06T10:00",
    "temperature_2m": 14.2,
    "wind_speed_10m": 6.8
  }
}
temperatura = podatki["current"]["temperature_2m"]
enota = podatki["current_units"]["temperature_2m"]
print(f"Na Jesenicah je trenutno {temperatura} {enota}.")
"""

import requests

def trenutna_temperatura(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    parametri = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m"
    }
    odgovor = requests.get(url, params=parametri)
    podatki = odgovor.json()
    return podatki["current"]["temperature_2m"]


kraji = {
    "Ljubljana": (46.0569, 14.5058),
    "Maribor": (46.5547, 15.6459),
    "Jesenice": (46.4353, 14.0457),
}
temperature = {
    "Ljubljana": (46.0569, 14.5058),
    "Maribor": (46.5547, 15.6459),
    "Jesenice": (46.4353, 14.0457),
}

for ime, (lat, lon) in kraji.items():
    t = trenutna_temperatura(lat, lon)
    print(f"{ime}: {t} °C")
for 
