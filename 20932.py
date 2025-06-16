# 퀴즈 질문과 정답 설정

quiz_questions = [

    {

        "question": "파이썬의 창시자는 누구인가요?",

        "options": ["1. 리누스 토르발스", "2. 괴테", "3. 귀도 반 로섬", "4. 빌 게이츠"],

        "answer": "3"

    },

    {

        "question": "파이썬의 최신 버전은 무엇인가요?",

        "options": ["1. Python 2.7", "2. Python 3.10", "3. Python 3.9", "4. Python 4.0"],

        "answer": "2"

    },

    {

        "question": "파이썬에서 리스트를 선언하는 방법은?",

        "options": ["1. list = {}", "2. list = []", "3. list = ()", "4. list = <>"],

        "answer": "2"

    }

]

# 퀴즈 실행 함수

def run_quiz():

    score = 0  # 점수 초기화

    print("퀴즈에 오신 것을 환영합니다!\n")

    # 각 질문에 대해 반복

    for i, quiz in enumerate(quiz_questions, 1):

        print(f"질문 {i}: {quiz['question']}")

        for option in quiz['options']:

            print(option)



        # 사용자 입력 받기

        answer = input("정답을 선택하세요 (숫자로 입력): ")



        # 정답 확인

        if answer == quiz["answer"]:

            print("정답입니다!\n")

            score += 1

        else:

            print(f"틀렸습니다! 정답은 {quiz['answer']}입니다.\n")



    # 최종 점수 출력

    print(f"퀴즈가 끝났습니다. 총 점수: {score} / {len(quiz_questions)}")

# 퀴즈 실행

run_quiz()

