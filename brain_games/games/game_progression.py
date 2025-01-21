import random
from brain_games.cli import welcome_user


def generate_progression():
    start = random.randint(1, 100)  # Начало прогрессии
    step = random.randint(1, 10)    # Шаг
    length = 10                      # Длина прогрессии согласно заданию
    progression = [start + step * i for i in range(length)]

    missing_index = random.randint(0, length - 1)  # Случайный индекс
    missing_value = progression[missing_index]      # Пропущенное значение

    progression[missing_index] = '..'  # Замена числа на двоеточие

    return progression, missing_value


def ask_progression():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("What number is missing in the progression?")

    rounds = 3  # Количество раундов
    for _ in range(rounds):
        progression, missing_value = generate_progression()
        progression_str = ' '.join(map(str, progression))  # Преобразование в строку
        print(f"Question: {progression_str}")
        
        user_answer = int(input("Your answer: "))
        if user_answer == missing_value:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{missing_value}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")