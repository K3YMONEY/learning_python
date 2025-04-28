''' A program that checks if the number is divisible by both 3 and 5 '''

number = input("Enter number ")
number = int(number)

if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)
