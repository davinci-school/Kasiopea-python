def reseni():
  # NAČTENÍ VSTUPŮ
  namerene_body = int(input())
  nadmorske_vysky = [int(i) for i in input().split()]
  #print(namerene_body)
  #print(nadmorske_vysky)
  # ALGORITMUS ŘEŠENÍ
  nevyjede = 0
  for vyska in range(namerene_body-1):
    if nadmorske_vysky[vyska+1] - nadmorske_vysky[vyska] > 3:
      nevyjede = 1
      
  if nevyjede > 0:
    print("ne")
  else:
    print("ano")


# TADY ZAČÍNÁ PROGRAM
pocet_ukolu = int(input())
while pocet_ukolu > 0:
    pocet_ukolu -= 1
    reseni()
