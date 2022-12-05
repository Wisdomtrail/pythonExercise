count = 0
largest_so_far = float("-inf")
smallest_so_far = float("inf")
second_largest = 0
while count < 5:
    num = int(input("give me a number:"))
    if num > largest_so_far:
        second_largest = largest_so_far
        largest_so_far = num
    if num < smallest_so_far:
        smallest_so_far = num

    count += 1

print("The smallest number is:", smallest_so_far)
print("and the second largest is:", second_largest)
print("and the largest is:", largest_so_far)
