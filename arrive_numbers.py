import random

numbers = []
while len(numbers) < 100:
    tmp = random.randint(1, 100)
    if tmp not in numbers:
        numbers.append(tmp)
print(numbers)
