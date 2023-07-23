def is_prime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False

    max_divisor = int(number ** 0.5) + 1

    for divisor in range(3, max_divisor, 2):
        if number % divisor == 0:
            return False

        return True


if __name__ == "__main__":
    print(is_prime(17))
    print(is_prime(15))
    print(is_prime(-5))
    print(is_prime(0))
