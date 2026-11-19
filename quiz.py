class Quiz:
    def __init__(self, question: str, choices: list[str], answer: int):
        self.question = question
        self.choices = choices
        self.answer = answer

    def display(self, index: int) -> None:
        print("-" * 40)
        print(f"[문제 {index}] {self.question}\n")
        for i, choice in enumerate(self.choices, start=1):
            print(f"{i}. {choice}")
        print()

    def is_correct(self, user_answer: int) -> bool:
        return self.answer == user_answer

    def to_dict(self) -> dict:
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Quiz":
        if (
            not isinstance(data, dict)
            or len(data.get("choices", [])) != 4
            or not isinstance(data.get("answer"), int)
            or not (1 <= data["answer"] <= 4)
        ):
            raise ValueError("잘못된 퀴즈 데이터 형식입니다.")
        return cls(str(data["question"]), [str(c) for c in data["choices"]], data["answer"])

def get_default_quizzes() -> list[Quiz]:
    return [
        Quiz("Python의 창시자는 누구인가요?", ["Guido van Rossum", "Linus Torvalds", "James Gosling", "Bjarne Stroustrup"], 1),
        Quiz("Git에서 원격 저장소의 변경사항을 가져와 병합하는 명령어는?", ["git push", "git commit", "git pull", "git init"], 3),
        Quiz("Python에서 키(Key)와 값(Value) 쌍으로 저장하는 자료형은?", ["list", "tuple", "set", "dict"], 4),
        Quiz("데이터 저장에 널리 쓰이는 경량 텍스트 데이터 형식은?", ["JSON", "JPEG", "MP4", "PNG"], 1),
        Quiz("Python에서 오류 발생 가능 코드를 감싸는 예외 처리 키워드는?", ["catch", "try", "throw", "error"], 2),
    ]
