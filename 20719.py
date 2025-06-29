def add(x, y):

    return x + y


def subtract(x, y):

    return x - y


def multiply(x, y):

    return x * y


def divide(x, y):

    if y == 0:

        return "오류: 0으로 나눌 수 없습니다."

    return x / y


def calculator():

    print("계산기를 사용해보세요!")

    print("연산을 선택하세요:")

    print("1. 덧셈")

    print("2. 뺄셈")

    print("3. 곱셈")

    print("4. 나눗셈")

    while True:

        choice = input("원하는 연산을 선택하세요 (1/2/3/4): ")

        if choice in ('1', '2', '3', '4'):

            num1 = float(input("첫 번째 숫자를 입력하세요: "))

            num2 = float(input("두 번째 숫자를 입력하세요: "))

            if choice == '1':

                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':

                print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':

                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':

                print(f"{num1} / {num2} = {divide(num1, num2)}")

        else:

            print("잘못된 입력입니다. 다시 선택해주세요.")

        # 계속 계산할지 물어봄

        next_calculation = input("계속 계산하시겠습니까? (예/아니오): ")

        if next_calculation.lower() != '예':

            break


# 계산기 실행

calculator()
