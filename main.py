from game import QuizGame


def main() -> None:
    game = QuizGame(state_file="state.json")
    try:
        game.run()
    except (KeyboardInterrupt, EOFError):
        print("\n\n⚠️ 강제 종료가 감지되었습니다. 현재 데이터를 저장합니다...")
        game.save_state()
        print("👋 안전하게 종료되었습니다.")


if __name__ == "__main__":
    main()
