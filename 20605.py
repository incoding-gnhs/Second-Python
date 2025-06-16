def get_bmi(height_cm, weight_kg):

    height_m = height_cm / 100

    bmi = weight_kg / (height_m ** 2)

    return round(bmi, 1)

def recommend_clothes(temperature_c, height_cm, weight_kg):

    bmi = get_bmi(height_cm, weight_kg)

    # 체형 분류

    if bmi < 18.5:

        body_type = "마름"

    elif 18.5 <= bmi < 24.9:

        body_type = "정상"

    elif 25 <= bmi < 29.9:

        body_type = "과체중"

    else:

        body_type = "비만"

    # 날씨에 따른 기본 옷 추천

    if temperature_c >= 28:

        weather_outfit = "반팔 티셔츠, 반바지"

    elif 23 <= temperature_c < 28:

        weather_outfit = "얇은 셔츠, 면바지"

    elif 17 <= temperature_c < 23:

        weather_outfit = "긴팔 셔츠, 청바지"

    elif 10 <= temperature_c < 17:

        weather_outfit = "얇은 니트, 자켓, 긴 바지"

    elif 0 <= temperature_c < 10:

        weather_outfit = "코트나 점퍼, 니트, 기모 바지"

    else:

        weather_outfit = "패딩, 내복, 두꺼운 니트"

    # 체형에 따른 스타일 조언 (간단한 예)

    if body_type == "마름":

        style_tip = "여유 있는 핏으로 볼륨감을 더해보세요."

    elif body_type == "정상":

        style_tip = "대부분의 스타일이 잘 어울려요!"

    elif body_type == "과체중":

        style_tip = "단색 계열, 스트레이트 핏을 추천해요."

    else:  # 비만

        style_tip = "어두운 톤과 레이어링으로 슬림한 연출을 해보세요."

    # 최종 추천 출력

    print(f"🌡 현재 기온: {temperature_c}°C")

    print(f"📏 키: {height_cm}cm, ⚖️ 몸무게: {weight_kg}kg (BMI: {bmi}, 체형: {body_type})")

    print(f"\n👕 옷차림 추천: {weather_outfit}")

    print(f"💡 스타일 팁: {style_tip}")

# 예시 사용

recommend_clothes(12, 170, 65)

