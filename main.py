numbers = [] * 5
numbers.append(int(input()))
max = numbers[0]
min = numbers[0]

for i in range(1,5,1):
    numbers.append(int(input()))
    if max < numbers[i]:
        max = numbers[i]
    if min > numbers[i]:
        min = numbers[i]
total = sum(numbers) - max - min
print(total)
