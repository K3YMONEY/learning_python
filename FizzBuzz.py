''' a program that prints the numbers from 1 to 100
separated by space '''
def FizzBuzz():
    for k in range(1, 101):
        if k % 3 == 0 and k % 5 == 0:
            print('FizzBuzz', end='')
        elif k % 3 == 0:
            print('Fizz', end='')
        elif k % 5 == 0:
            print('Buzz', end='')
        else:
            print(k, end='')
print(FizzBuzz())

