import numpy as np
import matplotlib.pyplot as plt

# Значення ймовірності p від 0 до 1 з інтервалом 0.05
p = np.arange(0.01, 1.01, 0.05)

# Функція ентропії
H_i = -p * np.log2(p)

# Графік
plt.figure(figsize=(8, 6))
plt.plot(p, H_i, marker='o', color='green', label="Hi = -p * log2(p)")
plt.title("Графік функції ентропії Hi = -p * log2(p)")
plt.xlabel("Ймовірність p")
plt.ylabel("Ентропія Hi")
plt.grid(True)
plt.legend()

plt.show()
