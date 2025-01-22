import prompt
from brain_games.cli import welcome_user


def run_game(game_logic, rules):
    name = welcome_user()
    print(rules)
    correct_answers = 0
    max_rounds = 3

    while correct_answers < max_rounds:
        question, correct_answer = game_logic()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
