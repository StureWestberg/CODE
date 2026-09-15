ålder = int(input("Hur gammal är du?"))
if ålder == 17:
    print("Du är lika gammal som det flesta i EE25")
    
if ålder != 17:
    print("du är inte lika gammal som dom flesta i EE25")
else:
    print("du är lika gammal som det flesta i EE25")
    
if ålder >= 18:
    print("Du är en riktig unc!!!")
elif ålder < 17:
    print("du får inte ta körkort")
else:
    print("du får ta körkort nästa år")
    
namn = input("vad är ditt namn")

if namn == "Sture":
    print(" du heter samma sak somm mig")
elif namn == "Stule":
    print("så stavar man inte")
else:
    print("du heter inte samma sak som mig")
    
if ålder == 16 and namn == "Sture":
    print("Är du samma person som mig?")