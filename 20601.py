import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

# 데이터 불러오기 (가상의 CSV 경로)

df = pd.read_csv("seoul_bike_data.csv")

# 데이터 미리보기

print(df.head())

# 결측치 확인

print("결측치 수:\n", df.isnull().sum())

# 대여량 분석

print("\n가장 많이 대여된 요일:")

print(df.groupby("요일")["대여량"].mean().sort_values(ascending=False))

# 요일별 대여량 시각화

plt.figure(figsize=(10,6))

sns.barplot(data=df, x="요일", y="대여량", estimator='mean', palette='coolwarm')

plt.title("요일별 평균 자전거 대여량")

plt.xlabel("요일")

plt.ylabel("평균 대여량")

plt.show()