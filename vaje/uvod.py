
def hello():
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
    poštevanka()