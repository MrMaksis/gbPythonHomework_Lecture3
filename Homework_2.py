quantity = int(input("Введите количество элементов в массиве> "))
array = []
for i in range(quantity):
    array.append(int(input(f"Введите {i+1} число> ")))
xNum = int(input("Введите число X> "))

distances = [abs(elem - xNum) for elem in array]
closest_elem = array[distances.index(min(distances))]

print(closest_elem)