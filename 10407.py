import math

# 순열 계산 함수

def permutation(n, r):

    return math.factorial(n) // math.factorial(n - r)

# 조합 계산 함수

def combination(n, r):

    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

# 테스트 예시

n = 5  # 전체 원소의 개수

r = 3  # 뽑을 원소의 개수

print(f"{n}개 중 {r}개를 뽑는 순열(P({n}, {r}))은: {permutation(n, r)}")

print(f"{n}개 중 {r}개를 뽑는 조합(C({n}, {r}))은: {combination(n, r)}")

