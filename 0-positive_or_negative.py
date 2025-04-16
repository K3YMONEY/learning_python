# program that prints if a number is positive or negative

number = input("Enter a number: ")
number = int(number)

if number < 0:
    print(f"{number} negative")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is positive")



