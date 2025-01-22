from brain_games.engine import run_game
from brain_games.games.game_calculator import calc_game, RULES


def main():
    run_game(calc_game, RULES)


if __name__ == "__main__":
    main()
