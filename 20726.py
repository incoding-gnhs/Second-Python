def show_intro():

    print("\n 화학 I 과목 소개 ")

    print("화학 I은 물질의 구성, 성질, 변화에 대한 기초적인 개념을 배우는 과목입니다.")

    print("이 과정을 통해 우리는 자연 현상을 분자 수준에서 이해하게 됩니다.\n")

def list_topics():

    print("주요 학습 단원:")

    topics = [

        "1. 원자의 구조",

        "2. 주기율표와 원소의 성질",

        "3. 화학 결합",

        "4. 물질의 상태",

        "5. 화학 반응과 반응식",

        "6. 산과 염기"

    ]

    for topic in topics:

        print(f"  {topic}")

def explain_topic(choice):

    explanations = {

        1: "원자는 물질의 기본 입자로, 전자, 양성자, 중성자로 구성됩니다.",

        2: "주기율표는 원소를 성질에 따라 배열한 표로, 주기성과 족의 개념을 포함합니다.",

        3: "화학 결합에는 이온 결합, 공유 결합, 금속 결합이 있으며, 이는 원자 간 상호작용입니다.",

        4: "물질은 고체, 액체, 기체 상태로 존재하며, 입자의 운동에 따라 상태가 달라집니다.",

        5: "화학 반응은 물질이 새로운 물질로 바뀌는 과정이며, 반응식으로 나타냅니다.",

        6: "산은 수소 이온을 내놓고, 염기는 수산화 이온을 내놓는 물질로 pH 개념이 있습니다."

    }

    print(f"\n {explanations.get(choice, '해당 번호의 단원이 없습니다.')}\n")

def main():

    while True:

        print("\n=== 화학 I 프로그램 ===")

        print("1. 과목 소개 보기")

        print("2. 학습 단원 보기")

        print("3. 단원별 설명 보기")

        print("4. 종료")

        choice = input("번호를 선택하세요: ")

        if choice == '1':

            show_intro()

        elif choice == '2':

            list_topics()

        elif choice == '3':

            list_topics()

            try:

                topic_num = int(input("\n보고 싶은 단원 번호를 입력하세요 (예: 1~6): "))

                explain_topic(topic_num)

            except ValueError:

                print("숫자를 입력해주세요.")

        elif choice == '4':

            print("프로그램을 종료합니다. 감사합니다!")

            break

        else:

            print("올바른 번호를 선택해주세요.")

if name == "__main__":

    main()

