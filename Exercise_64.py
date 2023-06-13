def print_numbers(n):
    if n <= 0:
        return
    else:
        print(n, end=", ")
        print_numbers(n - 1)

# Пример использования
N = 5
print_numbers(N)
print()
N = 8
print_numbers(N)