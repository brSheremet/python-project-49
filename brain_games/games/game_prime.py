import random

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'

MIN_NUMBERS = 1
MAX_NUMBERS = 100


def is_prime(num):
    if num < 2:  # Число меньше 2 не являются простыми
        return False
    if num in (2, 3):
        return True
    if num % 2 == 0 or num % 3 == 0:  # Исключаем кратные 2 и 3
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:  # Делится без остатка
            return False
        i += 6
    return True


def prime_game():
    num = random.randint(MIN_NUMBERS, MAX_NUMBERS)
    question = str(num)
    correct_answer = 'yes' if is_prime(num) else 'no'
    return question, correct_answer