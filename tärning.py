import random
ditt_slag = random.randint(1,6)
datorns_slag = random.randint(1,6)
print(f"Du slog:{ditt_slag}")
print(f"Datorns slog:{datorns_slag}")
if ditt_slag > datorns_slag:
    print("DU VANN!!")
else:
    print("Tyvärr vann datorn den här gången")
