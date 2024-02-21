numbers = [2, 2, 3, 4, 5, 6, 3]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
numbers.append(7)
print(numbers)
numbers.remove(6)
print(numbers)
numbers.insert(5, 8)
print(numbers)
print(4 in numbers)
print(10 in numbers)
numbers.pop()
print(numbers)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)