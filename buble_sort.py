pocet_uloh = int(input())
while pocet_uloh > 0:
    pozice = 0
    pocet_uloh -= 1
    pocet_cisel = int(input())  #3
    cisla = [int(i) for i in input().split()]  #[66 17 36 17 75 85 33 93]

    for index2 in range (pocet_cisel):            # [17 17 33 36 66 75 85 93]
        for index in range(pocet_cisel - 1):      # 0  
            if  cisla[index] > cisla[index + 1]:  #  
                aktualni_cislo = cisla[index]     # 
                cisla[index] = cisla[index + 1]   # []
                cisla[index + 1] = aktualni_cislo # []

    print(cisla)