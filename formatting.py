name = "sunday"
age = 18

s = f"{name} is {age} years old, and {name} loves java"
print(s)

hello = "Hello world"
to_be_found = "d"
for i, l in enumerate(hello):
    if l == to_be_found:
        print(f"{l}--->{i}")
        break

for index in range(len(hello)):
    print(f"({hello[index]}, {index})")
