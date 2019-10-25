# Isaac Waide
# October 14, 2019
# Hartwick Bakery

import statistics
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


def mean(cookies):
    total = 0
    for num in cookies:
        total = total + num
    return total / len(cookies)


def mean(candy):
    total = 0
    for num in candy:
        total = total + num
    return total / len(candy)


def cookiesAvg():
    return statistics.mean(cookies)


def cookies_max():
    print(max(cookies))


def cookies_min():
    print(min(cookies))


def candyAvg():
    return statistics.mean(candy)


def candy_max():
    print(max(candy))


def candy_min():
    print(max(candy))


cookies_input()
candy_input()

print(cookiesAvg)
print(cookies_max())
print(cookies_min())
print(mean(cookies))

print(candyAvg)
print(candy_max())
print(candy_min())
print(mean(candy))



