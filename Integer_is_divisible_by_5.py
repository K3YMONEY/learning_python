''' A program that checks if an integer is divisible by 5 '''
number = input("Enter number ")
number = int(number)

if number % 5 == 0:
    print(f"{number} is divisible by 5")
else :
    print(f"{number} is not divisible by 5")

