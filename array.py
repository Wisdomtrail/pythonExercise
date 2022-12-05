def outlier(array):
    odd_num = sum(digit % 2 for digit in array)
    remove = int(odd_num < 2)
    return next(digit for digit in array if digit % 2 == remove)


print(outlier([2, 4, 6, 7, 8, 10]))
print(outlier([1, 3, 5, 6, 7, 9]))
