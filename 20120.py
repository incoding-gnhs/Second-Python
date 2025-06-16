first = int(input("첫 번째 항을 입력하세요: "))

diff = int(input("공차를 입력하세요: "))

n = int(input("몇 번째 항까지 출력할까요? "))

for i in range(n):

  term = first + i * diff

  print(term, end=' ')