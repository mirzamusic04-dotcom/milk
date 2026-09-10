
"""def hello():
    oddelek = input("Kateri oddelek si? ")
    if oddelek.lower() == "1.ri":
          print(f"Hello {oddelek} ")
  
def poštevanka():
     x = int(input("izberi si število: "))
     št = 1
     while št <= 10:
          print(f"{št} * {x} = {št * x}")
          št += 1
 
if __name__ == "__main__":
    # To je moj prvi program
    # hello()
    poštevanka()"""

"""x = 5
y = 15
z = -10

# potenca
print(10**3)

# decimalna (float) števila

x = 3.14
Y = 10.012

print(0.5 + 0.5 == 1)
print((0.1 + 0.2) - 0.3)

# string - niz znakov
ime = "Luka"
print(ime)
print(len(ime))

st = "22"
print(st+st)
print(st * 100)

print(int(st) + 100)

naslov = "kidričeva 55"

print(naslov.upper())
print(naslov.lower())
naslov = naslov.strip()
print(len(naslov))"""

ime = "luka Colarič" #L.C
ime = ime.upper() # LUKA COLARIČ
spltIme = ime.split()
print(type(spltIme))
print(spltIme)

ime = spltIme[0][0] #"LUKA"[0]
pri = spltIme[1][0] #"COLARIČ"         altgr f+g

print(ime, pri)
print(f"{ime}.{pri}")