import datetime

import holidays

def get_korean_holidays_by_month(month: int, year: int = None):

    """

    사용자가 원하는 연도와 월을 입력하면 그 달의 대한민국 공휴일을 반환합니다.

    year가 입력되지 않으면 올해를 기준으로 합니다.

    month: 1~12 사이의 정수

    """

    if year is None:

        year = datetime.date.today().year

    kr_holidays = holidays.KR(years=year)

    result = []

    for date, name in sorted(kr_holidays.items()):

        if date.month == month:

            result.append(f"{date.strftime('%Y-%m-%d')} : {name}")

    return result

# 사용 예시

if name == "__main__":

    month = int(input("원하는 월을 입력하세요 (예: 11): "))

    year = input("연도를 입력하세요 (엔터시 올해): ")

    year = int(year) if year.strip() else None

    holidays_in_month = get_korean_holidays_by_month(month, year)

    if holidays_in_month:

        print(f"{year or datetime.date.today().year}년 {month}월의 공휴일:")

        for h in holidays_in_month:

            print(h)

    else:

        print("해당 월에는 공휴일이 없습니다.")