"""
3-2 : 인덱스에 의미 부여하여 풀어보기 - 계수 정렬 (counting sort : 각 숫자가 몇번 나왔는지 세고 그 개수를 이용해 정렬하는 것)

"""

import sys

N=int(sys.stdin.readline()) # 의미 없음. 그냥 형식임. 뭐 반복횟수를 지정할 때 사용해도 되고..

count=[0]*1001
numbers=list(map(int, sys.stdin.readline().split()))

for number in numbers:
    count[number] +=1  #인덱스를 숫자값으로 의미부여 해서 데이터를 저장 !!

for i in range(1001):
    if count[i] != 0:
        for _ in range(count[i]):
            sys.stdout.write(str(i)+' ')





"""
1) map(함수, 반복가능한객체) 반복가능한데이터를 함수에 하나씩 적용해서 새로운 map객체를 만듦
map(str,[1,2,3])       # ['1', '2', '3']   문자열로 변환하는 함수

2) split() 
"hello world".split()   # ['hello','world'] 인자값 안주면 공백 분리, 구분자 ',' 지정하면 그걸로
(',',1) 구분자 + 분할 횟수 
1️⃣ sys.stdin.readline() ➡️ 한 줄 입력을 "문자열"로 받음 예) 3 5 7 1 입력 -> "3 5 7 1\n"
2️⃣ .split()             ➡️ 문자열을 공백 기준으로 나눠서 리스트로 반환 -> ["3", "5", "7", "1"]


- 계수 정렬 과정 -
입력 [3,3,1,5,3,0]

index: 0 1 2 3 4 5 (실제 숫자)
count: 1 1 0 3 0 1 (그 숫자가 등장한 횟수)

숫자를 등장한 횟수만큼 출력(정렬된 결과를 만드는 방법)
0, 1, 3, 3, 3, 5 

왜?  비교정렬(버블, 선택 삽입, 퀵 등) 원소들끼리 크기 비교 후 위치 이동 보다 매우 빠름
값이 정수(0~1000)일 때 쓰면 좋음

"""