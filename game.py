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

    def play_quiz(self) -> None:
        if not self.quizzes:
            print("\n⚠️ 등록된 퀴즈가 없습니다.")
            return

        total = len(self.quizzes)
        correct = 0
        print(f"\n📝 퀴즈를 시작합니다! (총 {total}문제)")

        for idx, quiz in enumerate(self.quizzes, start=1):
            quiz.display(idx)
            ans = self.get_valid_int("정답 입력 (1-4): ", 1, 4)
            if quiz.is_correct(ans):
                print("✅ 정답입니다!")
                correct += 1
            else:
                print(f"❌ 오답입니다! 정답은 {quiz.answer}번입니다.")

        score = round((correct / total) * 100)
        print("\n" + "=" * 40)
        print(f"🏆 결과: {total}문제 중 {correct}문제 정답! ({score}점)")
        if self.best_score is None or score > self.best_score:
            self.best_score = score
            print("🎉 새로운 최고 점수입니다!")
        print("=" * 40)

    def run(self) -> None:
        while True:
            self.display_menu()
            choice = self.get_valid_int("선택: ", 1, 5)
            if choice == 1:
                self.play_quiz()
            elif choice == 5:
                print("\n👋 게임을 종료합니다.")
                break
            else:
                print("🚧 준비 중인 기능입니다.")
