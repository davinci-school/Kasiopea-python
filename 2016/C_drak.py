pocet_uloh = int(input())
while pocet_uloh > 0:
    pocet_uloh = pocet_uloh - 1
    pocet_draku, pocet_rytiru = [int(i) for i in input().split()]
    seznam_draku = [int(i) for i in input().split()]
    seznam_rytiru = [int(i) for i in input().split()]
    celkova_cena = 0
    for vyska_draka in seznam_draku:
        drak_zabit = 0
        for vyska_rytire in seznam_rytiru:
            if vyska_rytire >= vyska_draka:
                seznam_rytiru.remove(vyska_rytire)
                celkova_cena += vyska_rytire
                drak_zabit = 1
                break
        if drak_zabit == 0:
            celkova_cena = -1
            break        
    print(celkova_cena)