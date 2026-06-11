import random

namn = "Användare"
ålder = 33
humör = "existentiell kris"
iq = random.randint(40, 200)

def profil():
    print(f"\n{namn}, {ålder} år, IQ: {iq}, humör: {humör}\n")

def komplimang():
    print(f"\nHej {namn}! Med ett IQ på {iq} är du... speciell.\n")

def avsluta():
    print(f"\nHej då {namn}. Det var underwhelming.\n")
    exit()

meny = {"1": ("Profil", profil), "2": ("Komplimang", komplimang), "3": ("Avsluta", avsluta)}

while True:
    for k, (label, _) in meny.items():
        print(f"[{k}] {label}")
    val = input("> ").strip()
    if val in meny:
        meny[val][1]()
    else:
        print("Fel val. Klassiskt.\n")