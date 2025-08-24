name = input("Anna nimesi: ")


print(f"Terve, {name}!")
import math


print("YMPYRÄN PINTA-ALA")
sade = float(input("Anna ympyrän säde (cm): "))
pinta_ala = math.pi * sade ** 2
print(f"Ympyrän pinta-ala on {pinta_ala:.2f} neliösenttimetriä\n")


print("SUORAKULMION PIIRI JA PINTA-ALA")
kanta = float(input("Anna suorakulmion kanta (cm): "))
korkeus = float(input("Anna suorakulmion korkeus (cm): "))
piiri = 2 * (kanta + korkeus)
pinta_ala = kanta * korkeus
print(f"Suorakulmion piiri on {piiri:.2f} cm")
print(f"Suorakulmion pinta-ala on {pinta_ala:.2f} cm²\n")


print("KOLME KOKONAISLUKUA")
luku1 = int(input("Anna ensimmäinen kokonaisluku: "))
luku2 = int(input("Anna toinen kokonaisluku: "))
luku3 = int(input("Anna kolmas kokonaisluku: "))
summa = luku1 + luku2 + luku3
tulo = luku1 * luku2 * luku3
keskiarvo = summa / 3
print(f"Lukujen summa on {summa}")
print(f"Lukujen tulo on {tulo}")
print(f"Lukujen keskiarvo on {keskiarvo:.2f}\n")


print("KESKIAIKAINEN MASSA → NYKYMASSA")
leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))


grammat = (
    leiviskat * 20 * 32 * 13.3 +
    naulat * 32 * 13.3 +
    luodit * 13.3
)


kilot = int(grammat // 1000)
jäännös_grammat = grammat % 1000

print(f"Massa nykymittojen mukaan: {kilot} kilogrammaa ja {jäännös_grammat:.2f} grammaa")


