# game.py 
from quiz import Quiz

DEFAULT_QUIZZES = [
    Quiz(
        question="마블 시네마틱 유니버스에서 타노스가 모은 인피니티 스톤의 개수는?",
        choices=["4개", "5개", "6개", "7개"],
        answer=3,
        hint="손가락 튕기기에 필요한 수"
    ),
    Quiz(
        question="영화 '기생충'의 감독은?",
        choices=["박찬욱", "봉준호", "김기덕", "이창동"],
        answer=2,
        hint="설국열차도 만든 감독"
    ),
    Quiz(
        question="영화 '인터스텔라'에서 주인공 쿠퍼의 딸 이름은?",
        choices=["앤", "머프", "케이트", "제인"],
        answer=2,
        hint="머피의 법칙에서 따온 이름"
    ),
    Quiz(
        question="해리포터에서 해리가 속한 기숙사는?",
        choices=["슬리데린", "래번클로", "후플푸프", "그리핀도르"],
        answer=4,
        hint="용감함을 상징하는 기숙사"
    ),
    Quiz(
        question="영화 '타이타닉'에서 배가 침몰한 연도는?",
        choices=["1910년", "1912년", "1914년", "1916년"],
        answer=2,
        hint="20세기 초, 짝수 연도"
    ),
    Quiz(
        question="'어벤져스: 엔드게임'에서 타임스톤을 지키는 닥터 스트레인지의 본명은?",
        choices=["스티븐 로저스", "스티븐 스트레인지", "스티븐 배너", "스티븐 스타크"],
        answer=2,
        hint="이름이 직책과 비슷"
    ),
]

# 추가

class QuizGame:
    """퀴즈 게임 전체를 관리하는 클래스"""

    def __init__(self):
        self.quizzes = []        # 퀴즈 목록
        self.best_score = 0      # 최고 점수
        self.load_data()         # 파일에서 데이터 불러오기

    def show_menu(self):
        """메뉴 출력"""
        print("\n" + "="*40)
        print("       🎯 나만의 퀴즈 게임 🎯")
        print("="*40)
        print("  1. 퀴즈 풀기")
        print("  2. 퀴즈 추가")
        print("  3. 퀴즈 목록")
        print("  4. 점수 확인")
        print("  5. 종료")
        print("="*40)

    def get_menu_choice(self):
        """메뉴 선택 입력 처리"""
        while True:
            try:
                choice = input("선택: ").strip()
                if choice == "":
                    print("⚠️ 입력이 없습니다. 1-5 사이의 숫자를 입력하세요.")
                    continue
                choice = int(choice)
                if 1 <= choice <= 5:
                    return choice
                else:
                    print("⚠️ 잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.")
            except ValueError:
                print("⚠️ 잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.")

    def run(self):
        """게임 메인 루프"""
        print("\n📂 게임을 시작합니다!")
        while True:
            try:
                self.show_menu()
                choice = self.get_menu_choice()

                if choice == 1:
                    self.play_quiz()
                elif choice == 2:
                    self.add_quiz()
                elif choice == 3:
                    self.show_quiz_list()
                elif choice == 4:
                    self.show_score()
                elif choice == 5:
                    self.save_data()
                    print("\n👋 게임을 종료합니다. 수고하셨습니다!")
                    break

            except KeyboardInterrupt:
                print("\n\n⚠️ 프로그램을 중단합니다. 데이터를 저장합니다...")
                self.save_data()
                print("💾 저장 완료. 안전하게 종료합니다.")
                break
            except EOFError:
                print("\n⚠️ 입력 스트림이 종료되었습니다. 안전하게 종료합니다.")
                self.save_data()
                break

    # 아직 구현 안 된 메서드 (다음 STEP에서 채움)
    def play_quiz(self):
        """퀴즈 풀기"""
        if not self.quizzes:
            print("\n⚠️ 등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해주세요.")
            return

        print(f"\n📝 퀴즈를 시작합니다! (총 {len(self.quizzes)}문제)")
        score = 0

        for i, quiz in enumerate(self.quizzes, 1):
            print("\n" + "-"*40)
            quiz.display(i)

            # 정답 입력 처리
            while True:
                try:
                    ans = input("\n정답 입력 (1-4, h=힌트): ").strip()

                    if ans == "":
                        print("⚠️ 입력이 없습니다.")
                        continue

                    # 힌트 요청
                    if ans.lower() == "h":
                        if quiz.hint:
                            print(f"💡 힌트: {quiz.hint}")
                        else:
                            print("💡 힌트가 없습니다.")
                        continue

                    ans = int(ans)

                    if not (1 <= ans <= 4):
                        print("⚠️ 1-4 사이의 숫자를 입력하세요.")
                        continue

                    # 정답 확인
                    if quiz.check_answer(ans):
                        print("✅ 정답입니다!")
                        score += 1
                    else:
                        print(f"❌ 오답입니다. 정답은 {quiz.answer}번 입니다.")
                    break

                except ValueError:
                    print("⚠️ 숫자를 입력하세요. (1-4, h=힌트)")

        # 결과 출력
        total = len(self.quizzes)
        percent = int(score / total * 100)

        print("\n" + "="*40)
        print(f"🏆 결과: {total}문제 중 {score}문제 정답! ({percent}점)")

        # 최고 점수 갱신
        if percent > self.best_score:
            self.best_score = percent
            print("🎉 새로운 최고 점수입니다!")
        else:
            print(f"📊 현재 최고 점수: {self.best_score}점")

        print("="*40)

        # 결과 저장
        self.save_data()     
        
    def add_quiz(self):
        """퀴즈 추가"""
        print("\n📌 새로운 퀴즈를 추가합니다.")
        print("(취소하려면 아무 입력 없이 Enter)\n")

        # 문제 입력
        question = input("문제를 입력하세요: ").strip()
        if question == "":
            print("⚠️ 취소되었습니다.")
            return

        # 선택지 4개 입력
        choices = []
        for i in range(1, 5):
            while True:
                choice = input(f"선택지 {i}: ").strip()
                if choice == "":
                    print("⚠️ 선택지는 비워둘 수 없습니다.")
                    continue
                choices.append(choice)
                break

        # 정답 번호 입력
        while True:
            try:
                ans = input("정답 번호 (1-4): ").strip()
                if ans == "":
                    print("⚠️ 입력이 없습니다.")
                    continue
                ans = int(ans)
                if not (1 <= ans <= 4):
                    print("⚠️ 1-4 사이의 숫자를 입력하세요.")
                    continue
                break
            except ValueError:
                print("⚠️ 숫자를 입력하세요. (1-4)")

        # 힌트 입력 (선택)
        hint = input("힌트 입력 (없으면 Enter): ").strip()

        # Quiz 객체 생성 후 목록에 추가
        new_quiz = Quiz(question, choices, ans, hint)
        self.quizzes.append(new_quiz)

        # 파일 저장
        self.save_data()

        print("\n✅ 퀴즈가 추가되었습니다!")
        print(f"📊 현재 퀴즈 수: {len(self.quizzes)}개")


    def show_quiz_list(self):
        print("\n🚧 준비 중입니다...")

    def show_score(self):
        print("\n🚧 준비 중입니다...")

    def load_data(self):
        self.quizzes = list(DEFAULT_QUIZZES)

    def save_data(self):
        pass

