import math


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    else:
        return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    assert is_prime(3)
    assert is_prime(13)
    assert is_prime(2)
    assert is_prime(19)


