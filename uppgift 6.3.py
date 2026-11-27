import random
tal = [random.randint(1, 1000) for i in range(100)]
minsta = min (tal)
största = max (tal)
medelvärde = sum(tal) / len(tal)
print("Minsta talet är:", minsta)
print("Största talet är:", största)
print("Medelvärdet:", medelvärde)