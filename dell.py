count = 0
largest_so_far =  float("-inf")

while count < 5:
    num = int(input("Enter a number"))
    if num > largest_so_far:
        largest_so_far = num
    count += 1
print("The largest number is:", largest_so_far)
