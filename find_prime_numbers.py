import sys
from pprint import pprint

try:
    number = int(sys.argv[1])
except IndexError:
    number = 10000


def find_prime_number(start_number, end_number):
    prime_numbers = []
    for i in range(start_number, end_number):
        count = 0
        for j in range(2, i + 1):
            if i % j == 0:
                count += 1
        if count > 1:
            continue
        elif count == 1:
            prime_numbers.append(i)

    return prime_numbers


pprint(find_prime_number(1, number))
