import random

# programsko sortiranje:
# brojevi = [9, 1, 2, 8, 5, 7, 4]

# brojevi.sort() # sortiranje od najmanjeg ka najvecem

# print(brojevi)

# brojevi.reverse() # redja brojeve iz liste u obrnutom redosledu,ako je sort pre, po obrnutom redosledu iz sorta
# print(brojevi)

# rucno sortiranje:

# od najmanjeg ka najvecem

# indeks "i" / krece se od indeksa 1, jer i-1 ili i+1 ako je na nuli ili sestici "i" puca
# jer pre indeksa 0 nema nista, ni posle indeksa 6 nema nista

    #      0  1  2  3  4  5  6 
# brojevi = [9, 1, 2, 8, 5, 7, 4]

# # x  y  
# # pravi se privremeno mesto "privremeno za 9 itd" tzv booble sort
# while True:
#     izvrsena_zamena = False
#     for i in range(1, len(brojevi)):
#         #    1            # 9
#         if brojevi[i] < brojevi[i-1]:
#             privremeno = brojevi[i]
#             brojevi[i] = brojevi[i-1]
#             brojevi[i-1] = privremeno
#             izvrsena_zamena = True
#     if izvrsena_zamena == False:
#         break
# print(brojevi)
    
# privremeno = 9

proizvodi = ["Mobilni", "Televizor", "Kompjuter"]
cene = [155.95, 180.35, 199.99]

for x in range(len(proizvodi)):
    print(proizvodi[x], ":", cene[x])

# automobili = ["Audi", "BMW", "Yugo", "Kia","Citroen", "Peugeot"]

# for x in range(len(automobili)):
#     if x == 0:
#         print(automobili[x])
#         print("Jeeee")

proizvodi = [
                ["Iphone 11", "Samsung S22", "Xiaomi X3"],       # indeks 0
                ["Acer", "Mc book", "Dell"],                     # indeks 1
                ["Ipad", "Samsung galaxy TAB", "Xiaomi tablet"]  # indeks 2

            ]

telefoni = ["Iphone 11", "Samsung S22", "Xiaomi X3"]
laptopovi = ["Acer", "Mc book", "Dell"]
tableti = ["Ipad", "Samsung galaxy TAB", "Xiaomi tablet"] 

# print(proizvodi[0][0])
# print(proizvodi[1][1])

# for kategorija in proizvodi:
#     for stavka in kategorija:
#         print(stavka)
   # print(kategorija[0], kategorija[1], kategorija[2])


# neka moja ideja

# print("Modeli telefona: ")
# for svi_telefoni in telefoni:
#     print(svi_telefoni)
# print("Modeli laptopova: ")
# for svi_laptopovi in laptopovi:
#     print(svi_laptopovi)
# print("Modeli tableta :")
# for svi_tableti in tableti:
#     print(svi_tableti)

# for i in range (len(proizvodi)):
#     #print(proizvodi[i])
#     for j in range(len(proizvodi[i])):
#         print(proizvodi[i][j])

hrana = [

        ["cokolada", "bombone", "palacinke"],
        ["sarma","musaka","kiseli kupus", "pecena paprika", "ajvar", "sopska"]
        
        ]

for kategorija in hrana:
        for jelo in kategorija:
            print("Naziv", jelo)
        
# ime = "Sofija"
# poruka = "Cao " + ime + "!!!" # jedna varijanta
# poruka = f"Cao  {ime} !!!" # bez "f" stampa i viticaste zagrade
# print(poruka)

# a = 10
# b = 15
# sabiranje = f"Sabiranje brojeva {a} i {b} je {a + b}"
# print(sabiranje)
     
biblioteka = []
while True:
    print("Odaberi komandu 1-unos, 2-prikaz, 3-brisanje, >3-izlaz")
    komanda = int(input("Unesite komandu: "))

    if komanda == 1:
        # unos knjige preuzmi podatke
        naslov = input("Unesite naslov: ")
        autor = input("Unesite autora: ")  # input() samo za tekst
        isbn = int(input("Unesite broj: ")) # int(input) je samo za unos brojeva
        biblioteka.append([naslov, autor,isbn])
        print("Dodata knjiga")
    if komanda == 2:
        for knjiga in biblioteka:
            for detalj in knjiga:
                print(detalj)
    # ovde se vrsi brisanje
    if komanda == 3:
        kljucna_rec = input("Unesite naziv knjige koju zelite da obrisem: ")
        for knjiga in biblioteka:
        # ovde se proveravaju detalji "knjiga"
            for detalj in knjiga:
                if detalj == kljucna_rec:
                    biblioteka.remove(knjiga)
                    print("Knjiga je obrisana")
        if komanda >3:
            break


























