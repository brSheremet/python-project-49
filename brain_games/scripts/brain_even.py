from brain_games.engine import run_game
from brain_games.games.game_even import get_question_and_answer, RULES


def main():
    run_game(get_question_and_answer, RULES)


if __name__ == "__main__":
    main()