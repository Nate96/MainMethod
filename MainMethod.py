def add_(x, y):
    return x + y


def subtract(x, y):
    return x - y


def is_higher_than_ten_(x):
    return x > 10


def check_operation(operation):
    return operation == 'a'


if __name__ == "__main__":
    num1 = int(input("Enter a number: "))

    if is_higher_than_ten_(num1):
        print("The number is higher than 10")
    elif num1 == 10:
        print("The number is 10")
    else:
        print("The number lower than 10")

    num2 = int(input("Enter a second number: "))

    symbol = input("press a for add or press s for subtract: ")

    if check_operation(symbol):
        z = add_(num1, num2)
        print(z)
    else:
        z = subtract(num1, num2)
        print(z)