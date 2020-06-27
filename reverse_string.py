user_string = input("Please enter string")
reversed_string = ""

for item in range(len(user_string) -1, -1, -1):
    reversed_string += user_string[item]

print("reversed: " + reversed_string)
