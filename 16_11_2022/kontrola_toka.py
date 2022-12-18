import random

# x = -10
# if x > 0:
#     print("broj x je pozitivan") # nista se ne desava jer je x manji od 0, odnosno False

# x = 10
# if x > 0:
#     print("broj x je pozitivan.") # rezultat je print jer je x True

# print("izvrsava se u svakom slucaju.") # ova linije se izvrsava jer je nema uvlaku i nije usloveljena nicim   

# vozilo_u_pokretu = True
# brzina = 60

# if vozilo_u_pokretu:  # kad je if, nepotrebno je pisati True ili False, jer samo ako je true bice izvrsen sledeci kod
#                         # sto se vidi u promenljivoj
#     print("vozilo se krece...") # print se izvrsava samo ako je True
#     print("proverite i brzinu.")
#     if brzina > 50:
#         print("prekoracena brzina.")

#     print("ovo izvrsavam kolika god je brzina.")
#     if brzina <= 50:
#         print("Brzina je ok.")
# if vozilo_u_pokretu == False:
#     print("Vozilo se ne krece.")


#   1 - prikaz, 2 - kupovina, 3 - izlaz
# proizvod = "duks"  
# cena = 3000

# komanda = int(input("Unesite komandu: "))


# if komanda == 1:
#     print("Prikazi proizvode...")
#     print("Proizvod: ", proizvod, "Cena: ", cena)
# if komanda == 2:
#     print("Kupovina:")
#     stanje = int(input("Unesite stanje: "))
#     if stanje >= 3000:
#         print("Uspesna kupovina!")
#     if stanje < cena:
#         print("Neuspesna kupovina!")
# if komanda == 3:
#     print("Izlaz.")

# broj = -5
# if broj > 0:
#     print("Broj je veci od nule.")
# else: 
#     print("Broj je 0 ili manji od 0")

# marija = False
# ksenija = True
# katarina = False
# devojka_na_dejtu = ""

# if marija:
#     devojka_na_dejtu = "Marija"
# elif katarina:
#     devojka_na_dejtu = "Katarina"
# elif ksenija:
#     devojka_na_dejtu = "Ksenija"
# else:
#     devojka_na_dejtu = "Sofija"
# print("Izlazi sa mnom: ", devojka_na_dejtu)

# moja vezba 1
# proizvod = 1
# kupovina_proizvoda = 2
# izlazak_iz_programa = 3

# vrsta_proizvoda = "Duks"
# cena_proizvoda = 300

# komanda = int(input("Unesite komandu: "))

# if komanda == 1:
#     print("Naziv proizvoda: ", vrsta_proizvoda)
#     print("Cena: ", cena_proizvoda)
# if komanda == 2:
#     stanje = int(input("Unesite stanje: "))
#     if stanje >= 300:
#         print("Uspesna kupovina")
#     if stanje < 300:
#         print("Nemate dovoljno sredstava")
# if komanda == 3:
#     print("Hvala na poseti")       

# moja vezba 2
# tasterJePritisnut = True
# if tasterJePritisnut:
#     print("Taster je pritisnut")
#     tasterJePritisnut = False
# if not tasterJePritisnut: # ovde treba koristiti else
#     print("Taster nije pritisnut")
# else:
#     print("Taster nije pritisnut")

# moja vezba 3 probane sve tri varijante
# temperatura = 9
# if temperatura > 20:
#     print("Ponesite samo majicu")
# elif temperatura > 10:
#     print("Bice Vam potreban dzemper")
# else:
#     print("Ponesite jaknu")

# opet neka vezba
# kompjuter = random.randint(1, 2)
# rezultat = kompjuter
# korisnik = int(input("Unesite broj: "))
# if korisnik == kompjuter:
#     print("Cestitam, pobedili ste")
#     print("Kompjuter: ", rezultat)
# else:
#     print("Pokusajte ponovo")
#     print("Kompjuter: ", rezultat)

# automobil_polovan = False # nov
# godiste = 2022
# boja = "crna"

# if (automobil_polovan == True and godiste > 2017) and boja == "crna":
#     print("Kupujem")

# if not automobil_polovan:  # not pretvara false u true i obratno
#     print("Automobil je polovan")

# prisutan = False
# smer = "python"

# if prisutan and smer == "python": # if uvek ocekuje da bude nesto True
#     print("polaznik je bio na casu")


# if prisutan:
#     print("na casu")
# if not prisutan: # ako nas interesuje da li je na casu
#     print("nije na casu")
    
# trenutni_rezultat = random.randint(1, 100)
# novi_rezultat = int(input("Unesite broj (od 1 do 100):"))

# if novi_rezultat > 100 or novi_rezultat < 1:
#     print("Proverite broj, dozvoljeno od 1 - 100")
# else:
#     print("Trenutni rezultat: ", trenutni_rezultat, "Novi: ", novi_rezultat)
#     if trenutni_rezultat < novi_rezultat:
#         print("Pobedili ste")
#     elif trenutni_rezultat == novi_rezultat:
#         print("Izjednacene vrednosti!!!")
#     else:
#         print("Izgubili ste")

# pol = input("Unesite pol: ")
# poruka =""
# if pol == "m": # do posle else duzi zapis
#     poruka = "hej mister"
#     print("Hey mister")
# else:
#     poruka = "hej miss"
#     print("Hey miss")

# poruka = "hej mister" if pol == "m" else "hej mis" # kraci zapis
# print(poruka)

# popularan_proizvod = ""
# jesen = False
# popularan_proizvod = "ajvar" if jesen else "sladoled"
# print(popularan_proizvod)


# trenutni_rezultat = random.randint(1, 100)  # malo vezbanja
# novi_rezultat = int(input("Unesite novi broj od 1, 100: "))

# if novi_rezultat < 1 or novi_rezultat > 5:
#     print("Unesite broj od 1 - 100!!!")
# else:
#     print("Novi rezultat: ", novi_rezultat)
#     print("Trenutni rezultat: ", trenutni_rezultat)
#     if novi_rezultat > trenutni_rezultat:
#         print("Pobedili ste")
#     elif novi_rezultat < trenutni_rezultat:
#             print("Izgubili ste")
#     else:
#          novi_rezultat == trenutni_rezultat
#          print("Nereseno")



    











































