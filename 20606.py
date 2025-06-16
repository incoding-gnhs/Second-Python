def calculator():

    print("간단한 계산기입니다.")

    num1 = float(input("첫 번째 숫자를 입력하세요: "))

    op = input("연산자를 입력하세요 (+, -, *, /): ")

    num2 = float(input("두 번째 숫자를 입력하세요: "))

    if op == '+':

        result = num1 + num2

    elif op == '-':

        result = num1 - num2

    elif op == '*':

        result = num1 * num2

    elif op == '/':

        if num2 == 0:

            print("0으로 나눌 수 없습니다.")

            return

        result = num1 / num2

    else:

        print("지원하지 않는 연산자입니다.")

        return

    print(f"결과: {result}")

# 실행

calculator()

