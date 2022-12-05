num = int(input("Enter a number "))

while num == 0:
    print("No number entered")
    break

else:

    result = num
    count = 0
    if num < 0:
        negative = 1
    else:
        negative = 0
    if num > 0:
        positive = 1
    else:
        positive = 0
    while num != 0:
        count += 1
        num = int(input("Enter a number "))
        result += num
        if num < 0:
            negative += 1
        if num > 0:
            positive += 1

    print("total negative number is", negative)
    print("total positive is", positive)
    print("Total is", result)
    print("avearge is", result / count)
