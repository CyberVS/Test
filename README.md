https://www.onlinegdb.com/online_python_compiler

import random

нижче_число = int(input("Мінімум: "))
вище_число = int(input("Максимум: "))

загадане_число = random.randint(нижче_число, вище_число)

for спроба in range(7):
    вгадане_число = int(input(f"Спроба {спроба + 1}: Вгадай число: "))
    if вгадане_число == загадане_число:
        print("Ти вгадав!")
        break
    print("Занадто велике!" if вгадане_число > загадане_число else "Занадто мале!")
else:
    print(f"Не вгадав. Число було {загадане_число}.")
