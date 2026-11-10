# game.py 상단에 작성
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