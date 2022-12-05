num = int(input("Enter a number: "))

factors = 1
sum_of_factors = 0
while factors <= num // 2:
    if num % factors == 0:
        sum_of_factors += factors
    factors = factors + 1

if sum_of_factors < num:
    print(num, "has a deficient sum of factors")
elif sum_of_factors > num:
    print(num, "has an abundant sum of factors")
else:
    print(num, "has a perfect sum of factors")
    