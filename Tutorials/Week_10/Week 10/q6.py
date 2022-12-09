def sum_of_digit(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digit(n//10)

num = 345
print(sum_of_digit(num))