cisla = [35, 46, 76, 82, 75]
#       [0   1   2   3   4 ]  
print("dodkovo cislo je 46: ",cisla[1])
print("krystofovo je 75: ",cisla[4])
print("sebanovo je 82: ",cisla[3])




suma_dodko = 0
for cislo_dodko in range(5): #[0,1,2,3,4]
    suma_dodko += cislo_dodko

print("Dodko tip:", 10)  
print("vysledek:", suma_dodko)

suma_krystof = 0
for cislo_krystof in range(7): # [0,1,2,3,4,5,6]
    suma_krystof += cislo_krystof

print("Krystof tip:", 21)
print("vysledek:",suma_krystof)

suma_seban = 0
for cislo_seban in range(3): #[0,1,2]
    suma_seban += cislo_seban

print("Seban tip:", 3)
print("vysledek:",suma_seban)

