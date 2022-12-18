import random

# osoba = ["sofija", 25, "plava", False]

# for indeks in range(len(osoba)):
#     print(osoba[indeks])

# for osobina in osoba: # brzi nacin da se dobiju vrednosti iz niza, preskace se for
#     print(osobina)      # petlja sa "len"

# voce_i_povrce = ["jabuka", "beli luk", "crni luk", "banana", "mandarina", "krastavac"]

# for stavka in voce_i_povrce: # daje samo vrednost (jabuka,beli luk,crni luk...)
#     print(stavka)
    

# for i in range(len(voce_i_povrce)): 
#     #print(voce_i_povrce[i])  # daje samo indeks (moze se videti pod kojim je brojem) 
#     print("Na indeksu ", i, "Nalazi se ", voce_i_povrce[i]) # sa "len" je moguce videti
#                                                        # koji indeks necega je u listi

# for indeks, vrednost in enumerate(voce_i_povrce):
#     print("Indeks ", indeks, "Stavka ", vrednost)

# automobili = ["citroen", "bmw", "audi", "jugic", "opel", "porshe"]
 # zadatak: pozicija 0 auto citroen...

# for kola, modeli in enumerate(automobili):
    # print("Na poziciji: ", kola, "Model automobila: ", modeli)

# automobili.append("mercedes") # prosirenje liste radi se sa append
# automobili[2] = "audi a6" # uz pomoc [2], zavisno od pozicije menja se postojece mesto u listi
# print(automobili)
# del automobili[4] # brisanje necega iz liste preko indeksa bar mislim
# print(automobili)
# automobili.remove("bmw") # drugi nacin brisanja iz liste
# print(automobili)
# automobili.pop(0) # treci nacin brisanja iz liste preko indeksa bar mislim
# print(automobili)

#                 0        1       2       3        4       5         6
# automobili = ["citroen", "bmw", "audi", "jugic", "opel", "porshe", "pezo"]

# automobili_akcija = []

# for i in range(len(automobili)):
#     if i == 1 or i ==2 or i == 3:
#         automobili_akcija.append(automobili[i])
# print(automobili_akcija)

# automobili_akcija = automobili[1:4] # akcija preko slice 1, 2, 3
# print(automobili_akcija) 

# vezba

# brojevi = [1, 3, 8, 12, 25, 4, 6, 7, 19]

# parni = []
# neparni = []

# for broj in brojevi:
#     parni.append(broj) if broj % 2 == 0 else neparni.append(broj) # ternarni operator
#     # if broj % 2 == 0:
#     #     parni.append(broj)
#     # else: 
#     #     neparni.append(broj)
# print(parni, neparni)

# automobili = ["Mercedes", "Audi", "BMW", "Golf", "Pasat"]

# for kola, modeli in enumerate(automobili):
#     print("Na poziciji ", kola, "Nalazi se ", modeli)

# automobili.append("Jugo")
# print(automobili)

# automobili_akcija = []

# automobili_akcija = automobili[0:2]
# print(automobili_akcija)
# for x in range(len(automobili)):
#     if x == 1 or x == 2 or x ==3:
#         automobili_akcija.append(automobili[x])
# print(automobili_akcija)

# brojevi = [1, 3, 2, 6, 5, 18, 25, 8, 17]

# parni = []
# neparni = []

