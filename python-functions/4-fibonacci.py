def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_numbers = [0, 1]

        while len(fib_numbers) < n:
            next_fib = fib_numbers[-1] + fib_numbers[-2]
            fib_numbers.append(next_fib)

        return fib_numbers


if __name__ == "__main__":

    print(fibonacci_sequence(6))
    print(fibonacci_sequence(1))
    print(fibonacci_sequence(0))
    print(fibonacci_sequence(20))
