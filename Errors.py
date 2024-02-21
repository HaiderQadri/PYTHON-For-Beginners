try:
    age = int(input("Age: "))
    income = 10000
    risk = income / age
    print(f"Age {age} years")           # exit code 0 means program is completely executed but other than 0 means program is crashed.
except ValueError:
    print('Invalid Value')
except ZeroDivisionError:
    print('Age cannot be 0.')