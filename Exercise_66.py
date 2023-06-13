def sum_of_numbers(m, n):
    if m > n:
        return 0
    else:
        return m + sum_of_numbers(m + 1, n)

# Пример использования
M = 1
N = 15
result = sum_of_numbers(M, N)
print(result)
print()
M = 4
N = 8
result = sum_of_numbers(M, N)
print(result)