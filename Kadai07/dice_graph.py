import random

counts = [0] * 6

for _ in range(100):
    roll = random.randint(1, 6)
    counts[roll - 1] += 1

for i in range(6):
    print(f"{i+1}: {'*' * counts[i]}")

