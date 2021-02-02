pocet_uloh = int(input())
while pocet_uloh > 0:
  pocet_uloh = pocet_uloh -1
  pocet_radku, pocet_sloupcu = [int(i) for i in input().split()]
  prvni_radek = [int(i) for i in input().split()]
  for i in range(pocet_radku - 1):
    dalsi_radek = [int(i) for i in input().split()]
    for sloupec in range(pocet_sloupcu):
      prvni_radek[sloupec] += dalsi_radek[sloupec]
    
  for sloupec in range(pocet_sloupcu):
    prvni_radek[sloupec] %= 2 
  print(prvni_radek)