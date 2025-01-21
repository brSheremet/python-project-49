import random
from brain_games.cli import welcome_user


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def brain_gcd():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the greatest common divisor of given numbers.")
  
    for _ in range(3):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        print(f"Question: {num1} {num2}")
    
        correct_answer = gcd(num1, num2)
    
        answer = int(input("Your answer: "))
    
        if answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break

    else:  
        print(f"Congratulations, {name}!")