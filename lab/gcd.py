"""This project calculate the greatest common divisor of the two integer(Euclid’s algorithm)"""

def gcd(num1, num2):
    """This function gets two numbers, calculates the greatest common divisor and returns result"""
    if(num2 == 0):
        return num1
    else:
        return gcd(num2, num1 % num2)


if __name__ == "__main__":
    """You will input two numbers"""  
    print('The first number must be greater than the second')
    while True:
        number_1 = int(input('write number: '))
        number_2 = int(input('write number: '))  
        if number_2 > number_1:
            print('The first number must be greater than the second')
            continue
        else:
            result = gcd(number_1, number_2)
            print(f'The gcd of {number_1} and {number_2} is {result}')
            break