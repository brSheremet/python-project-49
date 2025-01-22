import random

RULES = 'Find the greatest common divisor of given numbers.'

MIN_NUMBER = 1
MAX_NUMBER = 100


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def game_gcd():
    num1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num2 = random.randint(MIN_NUMBER, MAX_NUMBER)

    question = f"{num1} {num2}"
    correct_answer = str(gcd(num1, num2))

    return question, correct_answer