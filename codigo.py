import random

dado = random.randint(1, 20)
bonus_fuerza = 5
tirada_de_fuerza = dado + bonus_fuerza

print(tirada_de_fuerza)

if tirada_de_fuerza > 15:
    print("Éxito en la tirada de fuerza")
else:
    print("Fallo en la tirada de fuerza")
