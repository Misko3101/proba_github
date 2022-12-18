import random

'''
 #######
  ######
   #####
    ####
     ###
      ##
       #
'''

# for x in range(10):
#     for y in range(10):
#         if y > x:
#             print("#", end="")
#         else:
#             print("", end=" ")
#     print()



kola = 0
cilj = 100
brzina = 10
gorivo = 10

while kola < cilj:
    print("voznja je u toku")
    kola += brzina
    gorivo -= 5
    if gorivo == 0: 
        break
else:
    print("stigli ste")



















