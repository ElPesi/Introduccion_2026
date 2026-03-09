def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def n_primo(n):
    count = 0
    num = 1

    while count < n:
        num += 1
        if is_prime(num):
            count += 1

    return num

print(n_primo(4))