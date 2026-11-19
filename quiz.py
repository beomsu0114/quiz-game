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
