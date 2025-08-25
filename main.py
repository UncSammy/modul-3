# 1. Kuha alamittainen vai ei
kuha = float(input("Anna kuhan pituus (cm): "))
if kuha < 37:
    puuttuu = 37 - kuha
    print(f"Laske kuha takaisin järveen, puuttuu {puuttuu:.1f} cm.")
else:
    print("Kuha on sallittua pyyntimittaa.")

# 2. Laivan hyttiluokka
luokka = input("Anna hyttiluokka (LUX, A, B, C): ").upper()

if luokka == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif luokka == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif luokka == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif luokka == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka.")

# 3. Hemoglobiiniarvo
sukupuoli = input("Anna biologinen sukupuoli (mies/nainen): ").lower()
hemo = int(input("Anna hemoglobiiniarvo (g/l): "))

if sukupuoli == "nainen":
    if hemo < 117:
        print("Hemoglobiiniarvo on alhainen.")
    elif hemo <= 175:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on korkea.")
elif sukupuoli == "mies":
    if hemo < 134:
        print("Hemoglobiiniarvo on alhainen.")
    elif hemo <= 195:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on korkea.")
else:
    print("Virheellinen sukupuoli.")

# 4. Karkausvuosi
vuosi = int(input("Anna vuosiluku: "))
if (vuosi % 4 == 0 and vuosi % 100 != 0) or (vuosi % 400 == 0):
    print(f"{vuosi} on karkausvuosi.")
else:
    print(f"{vuosi} ei ole karkausvuosi.")
