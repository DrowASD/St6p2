def count_divisors(X):
    count = 0
    for i in range(1, int(X ** 0.5) + 1):
        if X % i == 0:
            count += 2
            if i * i == X:
                count -= 1
    return count

X = int(input("Введите натуральное число X: "))
print("Количество натуральных делителей числа X:", count_divisors(X))
