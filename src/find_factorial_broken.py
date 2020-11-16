"""
script to find the factorial of a number
"""


def factorial(number):
    """
    function to compute the factorial of a number
    :param number: integer greater than zero
    :return: factorial of the input
    # DOCTEST examples
    #>>> 0
    1
    #>>> 6
    720
    """
    int(number)

    if number < 0:
        raise ValueError("Factorial of numbers less than zero is not possible")

    if 0 >= number <= 1:
        return 1

    # set global state
    factorial_sum = 1

    while number > 0:
        # insert error
        factorial_sum = factorial_sum * numberrrr
        number -= 1
        print(f"{number}  factorial_sum of this step = {factorial_sum:,}")

    return factorial_sum


if __name__ == '__main__':
    INPUT_NUMBER = int(input("Enter a number: "))

    print(f"{INPUT_NUMBER}  factorial = {factorial(INPUT_NUMBER)}")