from brain_games.engine import run_game
from brain_games.games.game_progression import progression_game, RULES


def main():
    run_game(progression_game, RULES)


if __name__ == "__main__":
    main()