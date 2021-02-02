# 3 - pocet uloh
# 3
# 65 22 31

pocet_uloh = int(input())
while pocet_uloh > 0:
  pocet_uloh -= 1

  pocet_cisel = int(input())
  cisla = [int(i) for i in input().split()] 
  print(cisla)
  print("nejmenší číslo je ",min(cisla))

  







# ukazka vstupu 
# 4 - nase cilova zastavka
# 1 8 3 4 - kolik stanic jedeme z kazde zastavky
# [2 10 6 8]
# ukazka vystupu
# 2 - kolik vlaku jsme pouzili


#def reseni():
#    cilova_stanice = int(input())    
#    #print(cilova_stanice)
#    pocet_zastavek = [int(i) for i in input().split()]
#    pocet_domecku = len(pocet_zastavek)
#    #print(pocet_stanic) 
#    for i in range(): #[0,1,2,3]
#        print(pocet_zastavek[i])


    
#pocet_zadani = int(input())
#while pocet_zadani > 0:
#    pocet_zadani -=1
#    reseni()