from datetime import date
from randomtimestamp import random_date


def birthdate():
    random_birthdate = random_date(start=date(1960, 1, 1),
                                   end=date(2005, 1, 1))

    return random_birthdate


# print(birthdate())
