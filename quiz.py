class Quiz:
    """개별 퀴즈를 표현하는 클래스"""

    def __init__(self, question, choices, answer, hint=""):
        self.question = question    # 문제
        self.choices = choices      # 선택지 리스트 (4개)
        self.answer = answer        # 정답 번호 (1~4)
        self.hint = hint            # 힌트 (보너스)

    def display(self, number):
        """퀴즈 출력"""
        print(f"\n[문제 {number}]")
        print(self.question)
        for i, choice in enumerate(self.choices, 1):
            print(f"  {i}. {choice}")

    def check_answer(self, user_answer):
        """정답 확인 - True/False 반환"""
        return user_answer == self.answer

    def to_dict(self):
        """JSON 저장용 딕셔너리 변환"""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
            "hint": self.hint
        }

    @staticmethod
    def from_dict(data):
        """딕셔너리에서 Quiz 객체 생성"""
        return Quiz(
            question=data["question"],
            choices=data["choices"],
            answer=data["answer"],
            hint=data.get("hint", "")
        )