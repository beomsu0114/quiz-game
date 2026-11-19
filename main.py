from game import QuizGame


def main() -> None:
    game = QuizGame()
    try:
        game.run()
    except (KeyboardInterrupt, EOFError):
        print("\n\n⚠️ 강제 종료가 감지되어 안전하게 종료합니다.")


if __name__ == "__main__":
    main()
