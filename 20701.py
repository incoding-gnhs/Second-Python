import requests

from datetime import datetime

import pytz

# 사용자의 시간 입력 받기

def get_user_time():

    input_time = input("시간을 입력하세요 (예: 2025-05-22 20:00): ")

    input_time = datetime.strptime(input_time, "%Y-%m-%d %H:%M")

    input_time = pytz.timezone('Asia/Seoul').localize(input_time)  # 서울 표준시로 설정

    return input_time

# 태양계 행성의 위치를 API를 통해 가져오는 함수

def get_planet_positions():

    url = "https://api.le-systeme-solaire.net/rest/bodies/"

    response = requests.get(url)

    data = response.json()



    planets_position = []

    for planet in data['bodies']:

        # 행성의 영어 이름과 공전 반지름(단위: 천문단위 AU)을 가져옴

        if planet.get('isPlanet', False):  # 행성만 필터링

            planets_position.append({

                'name': planet['englishName'],

                'semimajorAxis': planet['semimajorAxis'] if 'semimajorAxis' in planet else 'N/A',

                'isVisible': is_planet_visible(planet)

            })



    return planets_position

# 행성이 볼 수 있는지 확인하는 함수 (간단한 기준: 공전 반지름)

def is_planet_visible(planet):

    # 공전 반지름(AU)을 기준으로, 볼 수 있는지 여부를 간단히 판단 (예시: 가까운 행성은 보일 가능성 높음)

    semimajor_axis = planet.get('semimajorAxis', None)



    if semimajor_axis and isinstance(semimajor_axis, (int, float)):

        # 예시: 공전 반지름이 2AU 이하인 행성은 보일 가능성이 더 높다고 가정

        if semimajor_axis < 2:

            return "O"  # 볼 수 있음

        else:

            return "X"  # 볼 수 없음

    return "X"  # 반지름 정보가 없으면 볼 수 없음

# 서울에서 행성 위치 출력

def show_planet_info(input_time):

    print(f"시간: {input_time}")

    print("현재 위치에서 볼 수 있는 행성들:")



    planets_position = get_planet_positions()



    for planet in planets_position:

        print(f"{planet['name']} - 볼 수 있음 여부: {planet['isVisible']}")

if name == "__main__":

    input_time = get_user_time()  # 사용자 입력 시간 받기

    show_planet_info(input_time)  # 행성 정보 출력

