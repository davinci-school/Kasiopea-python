pocet_uloh = int(input())
while pocet_uloh > 0:
  pocet_uloh = pocet_uloh - 1 
  pocet_barev_a_pocet_ponozek = [int(i) for i in input().split()]
  pocet_barev = pocet_barev_a_pocet_ponozek[1]
  pocet_ponozek = pocet_barev_a_pocet_ponozek[0]
  ponozky = [int(i) for i in input().split()]
  liche = 0
  for idx_barvy in range(pocet_barev):
      pocet_ponozek_barvy = ponozky.count(idx_barvy + 1)
      ##print("pocet_ponozek_barvy ",idx_barvy+1,"je ",pocet_ponozek_barvy)
      liche += pocet_ponozek_barvy % 2 
  print("celkem liche ",liche)