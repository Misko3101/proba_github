import random
# clanovi u sekvencama uvek imaju indeks 0, 1, 3...
#           0       1     2       3
# osoba = ["sofija", 20, "plava", True]
# print(osoba)

# print(osoba[0])
# print("Godine: ", osoba [0], osoba [1])

# automobili = ["Mercedes", "Audi", "BMW"]
# print(automobili [1])

# for x in range(5, 10, 2): # 2 znaci da se broji po 2: 5, 7, 9
#     print(x)

     #  012345
kurs = "python"  # svako slovo u stringu je indeksirano brojem, kao iznad sto sam stavio
# print(kurs[0])
# print(kurs[1])
# print(kurs[2])
# print(kurs[3]) # itd


# for x in range(len(kurs)):
#     print("Na poziciji :",x, kurs[x])

# len odredjuje duzinu neke sekvence - len(kurs)

ustanova = "IT Academy"

# for indeks in range(len(ustanova)):
#     print(ustanova[indeks])
#     print("Ustanova: ", x, [ustanova])

primer = "zadatak1"

for zadatak in range(len(primer)):
    print(primer[zadatak], end="")

broj_karatktera = len(primer)
indeks = 0

while indeks < broj_karatktera:
    print(primer[indeks])
    indeks += 1

korisnicko_ime = "admin"
uneto_kor_ime = input("Unesi korisnicko ime: ")

if korisnicko_ime == uneto_kor_ime.lower(): # lower() pretvara velika slova u mala, upper() obratno
    print("Dobro dosli")
else:
    print("Pogresni podaci")


