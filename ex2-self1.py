# 디버깅 연습
"""
# 1.“합계가 이상하게 나오는 코드” # 기대값: 15  실제값: ?
total = 0
nums = [1,2,3,4,5]

for i in range(1, len(nums)):
    total += nums[i]
print(total)
"""

"""
#문제 2 — “while 루프
i = 0

while i < 5:
    print(i)
    i = i + 2
"""


# 3 — “리스트에 값이 안 쌓이는 이유 찾기”
numbers = []
# for i in range(5):
#     numbers.append(i*i)
# print(numbers)


# 일부러 버그 넣고 디버깅해보기 예:
for i in range(5):
    numbers = []
    numbers.append(i*i)

