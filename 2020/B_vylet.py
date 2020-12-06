pocet_zadani = int(input())
while pocet_zadani > 0:
    pocet_zadani -= 1
    min_teplota = 1000
    pocet_dni = int(input())
    teploty = [int(i) for i in input().split()]
    for den in range(pocet_dni-2):
        prvni_teplota = teploty[den]
        druha_teplota = teploty[den+1]
        treti_teplota = teploty[den+2]
        max_teplota=max(prvni_teplota,druha_teplota,treti_teplota)
        if min_teplota > max_teplota:
            min_teplota = max_teplota

    print("behem vyletu bude nejvyssi teplota ",min_teplota)        