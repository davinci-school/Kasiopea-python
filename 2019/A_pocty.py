def vyres():  
  # načítám vstup
  pocet_cisel = int(input())
  ciselna_rada = [int(i) for i in input().split()]
  
  # Algoritmus
  pocita_spravne = True
  for index in range(pocet_cisel):
    if (ciselna_rada[index] > 0) and (ciselna_rada[index] != index+1):
        pocita_spravne = False
  
  #vypisuji výstup
  if pocita_spravne:
    print("ano")
  else:
    print("ne")


pocet_uloh = int(input())
while pocet_uloh > 0:
  pocet_uloh -= 1
  vyres()