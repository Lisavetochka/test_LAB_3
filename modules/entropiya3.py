import math

# Функція для обчислення ентропії
def entropy(probs):
    return -sum(p * math.log2(p) for p in probs if p > 0)

# Ймовірності для трьох систем
sys_1 = [0.5, 0.2, 0.25, 0.05]
sys_2 = [0.25, 0.25, 0.25, 0.25]
sys_3 = [0.2, 0.3, 0.28, 0.22]

# Обчислення ентропії для кожної системи
entrp_1 = entropy(sys_1)
entrp_2 = entropy(sys_2)
entrp_3 = entropy(sys_3)

print('Ентропія системи 1 = ', round(entrp_1, 2))
print('Ентропія системи 2 = ', entrp_2)
print('Ентропія системи 3 = ', round(entrp_3, 2))
