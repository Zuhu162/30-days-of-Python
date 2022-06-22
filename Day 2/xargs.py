def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    print(total)


multiply(1, 2, 3, 4, 5, 6)
