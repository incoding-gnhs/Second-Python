# 사용자에게 이름과 나이를 입력받습니다

name = input("당신의 이름은 무엇인가요? ")

age = int(input("당신의 나이는 몇 살인가요? "))

print()  # 줄바꿈을 위해 공백 출력

print(f"안녕하세요, {name}님!")

# 나이에 따라 다른 메시지를 출력합니다

if age < 13:

    print("당신은 어린이입니다.")

elif age < 20:

    print("당신은 청소년입니다.")

elif age < 65:

    print("당신은 성인입니다.")

else:

    print("당신은 노년층입니다.")

print("좋은 하루 보내세요!")

