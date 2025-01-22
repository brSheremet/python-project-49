import random

RULES = 'What is the result of the expression?'

MIN_NUMBER = 1
MAX_NUMBER = 100


def calc_game():
    num1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num2 = random.randint(MIN_NUMBER, MAX_NUMBER)

    operation = random.choice(['+', '-', '*'])

    question = f"{num1} {operation} {num2}"

    correct_answer = str(eval(question))

    return question, correct_answer









