# 디버깅 연습 문제 1 — “리스트 합계가 이상하게 나오는 이유 찾기
# 기대 출력: 15
"""
nums = [1, 2, 3, 4, 5]
total = 0

for i in range(0, len(nums)):
    total += nums[i+1]

print(total)
"""
# 📌 포함된 버그 개수: 2
# 🎯 목표: 디버거로 i 값, nums 접근, IndexError 여부 확인
# 💡 힌트: WATCH에 i, nums[i], len(nums) 추가


# 디버깅 연습 문제 2 — “조건문이 항상 틀리게 동작하는 이유 찾기”
"""
x = 10

if x is 10:
    print("x is ten")
else:
    print("x is NOT ten")
"""

# 📌 버그 개수: 1
# 🎯 목표: “is” / “==” 차이 디버깅하며 확인
# 💡 힌트: VARIABLES에서 타입 확인해보기


# 디버깅 연습 문제 3 — “점수 평균이 항상 0.0 나오는 이유 찾기”
"""
scores = [80, 90, 100]
total = 0

for s in scores:
    total = total + s

avg = total / len(scores)
total = 0   # ???

print("평균:", avg)

"""
# 📌 버그 개수: 1
# 🎯 목표: avg가 잘 나왔는데도 0.0 되는 이유 추적
# 💡 힌트: 실행 순서 / 값 덮어쓰기


# 디버깅 연습 문제 4 — “while 루프가 1번도 실행되지 않는 이유 찾기”
"""
i = 10

while i < 5:
    print(i)
    i -= 1

"""
# 📌 버그 개수: 1
# 🎯 목표: while 조건을 디버깅 상태에서 직접 확인해보기
# 💡 힌트: breakpoint를 조건문 줄에 찍고 WATCH에 i 추가



# 디버깅 연습 문제 5 — “함수는 정상 같은데 반환값이 항상 None인 이유 찾기”
"""
def add(a, b):
    result = a + b
    print(result)

x = add(3, 5)
print("x =", x)

"""
# 📌 버그 개수: 1
# 🎯 목표: 함수 내부 단계별 step-into 실행 → return 유무 확인
# 💡 힌트: BREAKPOINT → F11 (Step Into) 사용 연습

"""
✅ 추천 풀이 흐름 (연습용)
1. 각 코드에 브레이크포인트 1개만 놓고 → F5 실행
2. VARIABLES / WATCH / CALL STACK 확인
3. F10 or F11 로 한 줄씩 확인
4. “내 예상과 실제 변수 값이 달라지는 순간” 찾기
5. 오류 원인 메모
6. 수정 코드 작성 + 정상 실행
"""