import random
from brain_games.cli import welcome_user

def get_question_and_answer():
    num1 = random.randint(1, 100)
    num2= random.randint(1, 100)

    operation = random.choice(['+', '-', '*']) #генерация случайной операции

    question = f"{num1} {operation} {num2}" #генерация вопроса

    correct_answer = eval(question)

    return question, correct_answer
def play_calculator_game():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("What is the result of the expression?")

    for _ in range(3):
        question, correct_answer = get_question_and_answer()
        print(f"Question: {question}")
        user_answer = int(input("Your answer: "))

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")






