def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def is_palindrome(number):
    return str(number) == str(number)[::-1]


def find_prime_palindrome(value):
    if value < 2:
        return 2

    if value % 2 == 0:
        value -= 1

    while True:
        value += 2
        if is_palindrome(value) and is_prime(value):
            return value






try:
    input_value = input("Enter a number: ")
    result = find_prime_palindrome(int(input_value))
    print(result)
except ValueError:
    print("Invalid input!")




