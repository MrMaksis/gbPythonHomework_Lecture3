import random

array = [random.randint(0, 10) for _ in range(10)]
print(array)

searchNum = int(input("Введите число для поиска> "))
current = 0
for i in range(0, len(array)):
    if array[i] == searchNum:
        current += 1
print(f"По вашему запросу найдено {current} число(сел)")
