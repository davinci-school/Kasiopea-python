zadani = int(input())
while zadani > 0:
  zadani -= 1

  # ukazka zadani 
  # 3
  # 2 6 8
  # ukazka vystupu
  # 3 (vyhrala treti uloha, protoze mela nejvic hlasu)
  # nacteme vstup
  pocet_uloh = int(input())
  hlasy = [int(i) for i in input().split()]

  # Algoritmus reseni
  max_pocet_hlasu = 0
  cislo_vitezne_ulohy = 0
  
  akt_pozice = 1            #akt_pozice = 2
  for akt_hlas in hlasy:    # akt_hlas = 6
 
    if akt_hlas > max_pocet_hlasu: # 6 > 2
        max_pocet_hlasu = akt_hlas  # 6
        cislo_vitezne_ulohy = akt_pozice  # 2
    
    akt_pozice += 1

  print(cislo_vitezne_ulohy)