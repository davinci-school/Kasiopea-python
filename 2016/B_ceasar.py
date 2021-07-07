# T ≤ 5
# Počet znaků včetně mezer ve zprávě nepřesáhne 250. 
# Posun je vždy o 4 písmena.

# 4 
# S DI LBEDO MKOCKB
# I TY BRUTE CAESAR
ABECEDA = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
pozice_R = 17
#print(len(ABECEDA))
zadani = int(input())
while zadani > 0:
  print("zadani",4- zadani)
  zadani -= 1
  pocet_slov = int(input())
  slova =  [i for i in input().split()]
  #posun = ?
  posledni_slovo = slova[-1]
  posledni_znak = posledni_slovo[-1]
  for idx, znak in enumerate(ABECEDA):
    if znak == posledni_znak:
        posun = 26 - pozice_R + idx
        
  for slovo in slova:
      #print(slovo)
      for pismeno in slovo:
          #print(pismeno)
          for idx, znak in enumerate(ABECEDA):
              if znak == pismeno:
                  print(ABECEDA[idx-posun])
      print(" ")