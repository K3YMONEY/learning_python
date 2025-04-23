''' write a program to show
if a number is even or odd '''

number = input("Enter number: ")
number = int(number)

if number % 2 == 0:
    print("{} is even".format(number))
else:
    print("{} is odd".format(number))
