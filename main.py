sum = 0
numbers = [0] * 10
user_input = int(input())
numbers[0] = user_input
max = numbers[0]
min = numbers[0]

for i in range(1,5,1):
    user_input = int(input())
    if max < user_input:
        max = user_input
    if min > user_input:
        min = user_input
    numbers[i] = user_input

for i in range(0,5,1):
    if numbers[i] == min:
        continue
    if numbers[i] == max:
        continue
    sum += numbers[i]
print(sum)