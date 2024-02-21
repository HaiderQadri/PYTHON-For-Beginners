numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[0] = 10
print(numbers)
print(numbers[4:8])
print(numbers[-2])
largest_number = numbers[0]
for number in numbers:
    if number > largest_number:
        largest_number = number
print(largest_number)
