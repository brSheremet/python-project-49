from brain_games.engine import run_game
from brain_games.games.game_even import even_game, RULES


def main():
    run_game(even_game, RULES)


if __name__ == "__main__":
    main()
