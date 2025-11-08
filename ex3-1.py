"""
3-1 시간 초과의 원인을 찾아 해결하기
input(), print() VS sys.stdin.readline(), sys.stdout.write()
"""

a=int(input())
print(a)

import sys
b=int(sys.stdin.readline())
sys.stdout.write(str(b) + '\n') # sys.stdout.write()은 문자열만 출력할 수 있음. 그래서 형변환 해줌


"""
& C:/Users/user/AppData/Local/Programs/Python/Python314/python.exe d:/codingTestPractice/ex3-1.py
& : powershell에서 명령 실행 연산자(실행하라는 의미)
C:/Users/.../python.exe : 실행할 파이썬 인터프리터 경로
이하 : 실행할 파이썬 스크립트(py 파일)경로
"""