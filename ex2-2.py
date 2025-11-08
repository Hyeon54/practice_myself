# p26 결함 있는 코드 예제
# 배열의 주어진 범위의 합을 2로 나눈 몫 구하기

import random

# 1. 디버깅시에는 seed(고정값) A[i] = random.randrange(1,101)
random.seed(42)

# 디버깅용 입력 고정
testcase =2 #원래 int(input())
tests = [(1, 3), (4, 6)] #t=1 ->(1,3) t=2 ->(4,6)

answer=0
A=[0]*(100001)

for i in range(0, 10001) :
    A[i] = random.randrange(1,101) 
print("A[0:10]", A[:10]) # 2. 디버깅 확인용 로그포인트

for t in range(1, testcase+1):
    start, end = tests[t - 1] # 디버깅용 고정값 map(int, input().split()) # 입력시에 strat하나 end하나 공백기준 2개

    #3.로그포인트
    print(f"[before] : t={t}, start = {start}, end={end}, answer={answer}")

    for i in range(start, end+1):
        answer = answer + A[i]
    
    print(str(testcase) + " " + str(answer/2))

# 오류랑 수정
# 1	answer 누적됨	테스트케이스별 초기화 없음	for t 내부에서 answer = 0
# 2	출력에서 testcase 출력	전부 같은 숫자 출력됨	t 또는 값만 출력해야 함
# 3	answer / 2	반으로 나눌 이유 없음	그냥 answer 출력
# 4	배열 값 10000개만 초기화	나머지는 전부 0 → 잘못된 합 가능	인덱스 범위 통일 필요
