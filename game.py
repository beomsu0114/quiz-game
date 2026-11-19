import json
import os
from quiz import Quiz, get_default_quizzes


class QuizGame:
    def __init__(self, state_file: str = "state.json"):
        self.state_file = state_file
        self.quizzes: list[Quiz] = []
        self.best_score: int | None = None
        self.load_state()

    def load_state(self) -> None:
        if not os.path.exists(self.state_file):
            self.quizzes = get_default_quizzes()
            self.best_score = None
            self.save_state()
            return
        try:
            with open(self.state_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.quizzes = [Quiz.from_dict(q) for q in data["quizzes"]]
            self.best_score = data.get("best_score")
            score_str = f"{self.best_score}점" if self.best_score is not None else "기록 없음"
            print(f"📂 저장된 데이터를 불러왔습니다. (퀴즈 {len(self.quizzes)}개, 최고점수 {score_str})")
        except (json.JSONDecodeError, KeyError, ValueError, OSError):
            print("⚠️ 데이터 파일이 손상되어 기본 퀴즈로 복구합니다.")
            self.quizzes = get_default_quizzes()
            self.best_score = None
            self.save_state()

    def save_state(self) -> None:
        data = {
            "quizzes": [q.to_dict() for q in self.quizzes],
            "best_score": self.best_score,
        }
        try:
            with open(self.state_file, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except OSError as e:
            print(f"⚠️ 데이터 저장 중 오류가 발생했습니다: {e}")

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

    def get_non_empty_str(self, prompt: str) -> str:
        while True:
            text = input(prompt).strip()
            if text:
                return text
            print("⚠️ 내용을 입력해주세요.")

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
            self.save_state()
            print("🎉 새로운 최고 점수입니다!")
        print("=" * 40)

    def add_quiz(self) -> None:
        print("\n📌 새로운 퀴즈를 추가합니다.")
        q = self.get_non_empty_str("문제를 입력하세요: ")
        choices = [self.get_non_empty_str(f"선택지 {i}: ") for i in range(1, 5)]
        ans = self.get_valid_int("정답 번호 (1-4): ", 1, 4)
        self.quizzes.append(Quiz(q, choices, ans))
        self.save_state()
        print("✅ 퀴즈가 추가되었습니다!")

    def list_quizzes(self) -> None:
        if not self.quizzes:
            print("\n⚠️ 등록된 퀴즈가 없습니다.")
            return
        print(f"\n📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print("-" * 40)
        for idx, quiz in enumerate(self.quizzes, start=1):
            print(f"[{idx}] {quiz.question}")
        print("-" * 40)

    def show_score(self) -> None:
        if self.best_score is None:
            print("\nℹ️ 아직 퀴즈를 풀지 않았습니다.")
        else:
            print(f"\n🏆 최고 점수: {self.best_score}점")

    def run(self) -> None:
        while True:
            self.display_menu()
            choice = self.get_valid_int("선택: ", 1, 5)
            if choice == 1:
                self.play_quiz()
            elif choice == 2:
                self.add_quiz()
            elif choice == 3:
                self.list_quizzes()
            elif choice == 4:
                self.show_score()
            elif choice == 5:
                self.save_state()
                print("\n👋 데이터를 저장하고 게임을 종료합니다.")
                break
