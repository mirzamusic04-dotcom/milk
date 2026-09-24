def vnos (s:list):
    while True:
        izdelek = input("vnesi: ").lower()
        if izdelek == "":
            break
        s.append(izdelek)

def izpis(s:list):
    print("-------------------")
    for index in range(len(s)):
        print(f"({index+1}) {s[index]}")

def briši (s:list):
    briši = input("briši: ").lower()
    print("briši:", end = "")
    while briši in s:
        s.remove(briši)
        print ("*", end="")
    print()    

def posodobi (s:list):
    pass



if __name__=="__main__":
    s = []
    vnos (s)
    izpis (s)
    briši (s)
    izpis (s)
    posodobi (s)
    izpis (s)