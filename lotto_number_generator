from random import randrange


def lotto_number_generator():
    lotto_number = []
    while len(lotto_number) < 6:
        new_lotto_number = randrange(1, 46)
        if new_lotto_number in lotto_number:
            continue
        else:
            lotto_number.append(new_lotto_number)
    return lotto_number


if __name__ == "__main__":
    print(lotto_number_generator())
