import string

user_input = input("Enter the word to encode: ")
key = int(input("what key would you like to use: "))

lower_letters = string.ascii_lowercase
decoded_letters = lower_letters[key:] + lower_letters[:key]

print(decoded_letters)
print(user_input.translate(str.maketrans(lower_letters, decoded_letters)))

