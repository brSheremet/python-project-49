from brain_games.engine import run_game
from brain_games.games.game_gcd import game_gcd, RULES


def main():
    run_game(game_gcd, RULES)


if __name__ == "__main__":
    main()
