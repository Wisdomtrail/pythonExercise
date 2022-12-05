num = int(input("Enter a number: "))

smallest_num = num
largest_num = num

while num != 0:

    if num > largest_num:
        largest_num = num

    if num < smallest_num:
        smallest_num = num
    num = int(input("Enter a number, enter 0 to exit: "))
print("largest num is", largest_num, "and smallest_num is", smallest_num)
