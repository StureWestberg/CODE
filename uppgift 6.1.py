antal = int(input("Hur många tal ska följden innehålla"))
talföljd = []
tal = 2
for i in range(antal):
    talföljd.append(tal)
    tal = tal * 3
print (talföljd)