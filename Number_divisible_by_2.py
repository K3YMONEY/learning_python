''' A program that prints "Even" if a number is divisible by 2
and "Odd" if otherwise '''

number = input(" Enter number ")
number = int(number)

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
