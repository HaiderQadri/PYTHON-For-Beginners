phone_number = input("Enter Phone Number: ")
number_transformation = {
    '0': 'Zero',
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine'
}
output = ""
for character in phone_number:
    output += number_transformation.get(character) + " "
print(output)
