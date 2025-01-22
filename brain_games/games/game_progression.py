import random

RULES = 'What number is missing in the progression?'

MIN_NUMBERS = 1
MAX_NUMBERS = 10
MIN_LENGTH = 5
MAX_LENGTH = 10
MIN_STEP = 1
MAX_STEP = 5


def progression_game():
    start = random.randint(MIN_NUMBERS, MAX_NUMBERS)
    step = random.randint(MIN_STEP, MAX_STEP)
    length = random.randint(MIN_LENGTH, MAX_LENGTH)
    progression = [start + step * i for i in range(length)]

    missing_index = random.randint(0, length - 1)
    missing_value = progression[missing_index]

    progression[missing_index] = '..'

    question = ' '.join(map(str, progression))

    return question, str(missing_value)