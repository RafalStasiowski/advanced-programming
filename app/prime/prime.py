def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True


def check_prime(number: int) -> bool:
    return is_prime(number)
