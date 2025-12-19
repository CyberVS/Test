import random

secret = random.randint(1, 10)
guess = int(input("Вгадай число від 1 до 10: "))

if guess == secret:
    print("🎉 Молодець! Ти вгадав!")
else:
    print("❌ Не вгадав. Було число:", secret)
    
