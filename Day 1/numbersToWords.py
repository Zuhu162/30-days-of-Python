numbers = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five"
}

phone = input("Phone: ")
output = ""
for ch in phone:
    output += numbers.get(ch, "!") + " "

print(output)