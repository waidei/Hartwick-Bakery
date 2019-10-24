# Isaac Waide
# October 14, 2019
# Hartwick Bakery

cookies = []
candy = []


def cookies_input():
    for ele in range(0, 6):
        value = int(input("Enter value for cookies sales"))
        cookies.append(value)


def candy_input():
    for ele in range(0, 6):
        value = int(input("Enter value for candy sales"))
        candy.append(value)


def mean(cookies_input):
    total = 0
    for num in cookies_input:
        total = total + num
    return total / len(cookies_input)


def mode(cookies_input()):
max_count = (0, 0)
for num in cookies_input:
        occurrences = cookies_input.count(num)
        if occurrences > max_count[0]:
            max_count = (occurrences, num)
return max_count[1]


cookies_input()
candy_input()
print(mean(cookies_input))
print(mode(cookies_input))
