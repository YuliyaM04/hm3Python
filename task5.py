# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

n = int(input('Введите число: '))

def fibonacci(n):
    f_nums = []
    a, b = 1, 1
    for i in range(n-1):
        f_nums.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (n):
        f_nums.insert(0, a)
        a, b = b, a - b
    return f_nums

f_nums = fibonacci(n)
print(fibonacci(n))


