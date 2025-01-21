import random
from brain_games.cli import welcome_user


def is_prime(num):
    if num < 2:  # Число меньше 2 не являются простыми
        return False
    if num in (2, 3):
        return True
    if num % 2 == 0 or num % 3 == 0:  # Исключаем кратные 2 и 3
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:  # Делится без остатка - не простые
            return False
        i += 6
    return True


def play_is_prime():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print(f'Answer "yes" if given number is prime. Otherwise answer "no".')

    for _ in range(3):
        num = random.randint(1, 100)
        print(f"Question: {num}")
        user_answer = input("Your answer: ").strip().lower()
        
        correct_answer = "yes" if is_prime(num) else "no"

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  + f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
