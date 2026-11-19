from quiz import Quiz, get_default_quizzes


class QuizGame:
    def __init__(self):
        self.quizzes = get_default_quizzes()
        self.best_score = None

    def get_valid_int(self, prompt: str, min_val: int, max_val: int) -> int:
        while True:
            raw = input(prompt).strip()
            if not raw:
                print(f"⚠️ 빈 입력입니다. {min_val}-{max_val} 사이의 숫자를 입력하세요.")
                continue
            try:
                val = int(raw)
            except ValueError:
                print(f"⚠️ 숫자가 아닙니다. {min_val}-{max_val} 사이의 숫자를 입력하세요.")
                continue
            if not (min_val <= val <= max_val):
                print(f"⚠️ 범위를 벗어났습니다. {min_val}-{max_val} 사이의 숫자를 입력하세요.")
                continue
            return val

    def display_menu(self) -> None:
        print("\n" + "=" * 40)
        print("        🎯 나만의 퀴즈 게임 🎯")
        print("=" * 40)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("=" * 40)

    def run(self) -> None:
        while True:
            self.display_menu()
            choice = self.get_valid_int("선택: ", 1, 5)
            if choice == 5:
                print("\n👋 게임을 종료합니다.")
                break
            else:
                print("🚧 준비 중인 기능입니다.")
