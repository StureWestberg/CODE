tid = int(input("hur länge pratar du i telefon i månaden"))

if tid < 33:
    print("Kontant är bäst för dig")
elif tid > 66:
    print("Du borde skaffa Plus")
else:
    print("Du borde skaffa Normal")