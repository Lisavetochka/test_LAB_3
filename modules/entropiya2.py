import math

# Ймовірності для системи, де один стан відомий точно
p1 = 0
p2 = 0
p3 = 1

# Функція для обчислення ентропії
def entropy(probs):
    return -sum(p * math.log2(p) for p in probs if p > 0)

# Обчислюємо ентропію
probs = [p1, p2, p3]
entropy_res = abs(entropy(probs))
print("Результат виконання програми:", entropy_res)
