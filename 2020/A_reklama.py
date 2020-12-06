pocet_zadani = int(input())
while pocet_zadani > 0:
    pocet_zadani -= 1
    a,b,c = [int(i) for i in input().split()]
    zisk_bez_reklamy = b
    zisk_s_reklamou = a - c
    if zisk_bez_reklamy < zisk_s_reklamou:
        print("NE REKLAMU")
    else:
        print("REKLAMU")