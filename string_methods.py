hello = "Hello there!!"

print(hello.find("o"))
print(hello.index("h"))
print(hello.rfind("e"))
print(hello.upper())
print(hello.lower())
print(hello.capitalize())
print(hello.title())
print(hello.casefold())
print(hello.swapcase())
print(hello.lower().count("e"))
print(hello.replace("l", "u", 1))
print(hello.partition("e"))
print(hello.split())
print("-".join(["a", "b", "c"]))
print(hello.strip())
bin_ = "101001110***10101#78"
print(bin_.replace("1", "x").replace("0", "1").replace("x", "0"))
print(bin_.translate(str.maketrans("01", "10", "8#!*")))
print(hello.index("o"))
print(hello.center(30, "-"))
for i in range(1, 21, 2):
   # h = "*" * i
    t = "*" * i
    y = "*" * i
    print(t.center(19), y.rjust(19))