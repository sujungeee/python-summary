import sys

# sys이용- 하나의 문자열 데이터 입력받기
input_data= sys.stdin.readline().rstrip()
print(input_data)

# 한 줄에 여러 개의 값을 입력 받기
a,b,c= input().split()
print('a: ', a)
print('b: ', b)
print('c: ', c)

# sys 이용: 한 줄에 여러 개의 값을 입력 받기
a2, b2, c2= sys.stdin.readline().split()
print('a2: ', a2)
print('b2: ', b2)
print('c2: ', c2)

#############################

# 특정 자료형 값 입력 받기
num= int(input())
print('num: ', num)

# sys 이용: 특정 자료형 값 입력 받기
num2= int(sys.stdin.readline())
print('num2: ', num2)

#############################

# 한 줄에 여러 개의 값을 특정 자료형으로 입력 받기
h, m= map(int, input().split())
print('h: ', h)
print('m: ', m)

# sys 이용: 한 줄에 여러 개의 값을 특정 자료형으로 입력 받기
h2, m2= map(int, sys.stdin.readline().split())
print('h2: ', h2)
print('m2: ', m2)

#############################

# 활용 (1): map형태를 list로도 변환 가능
# 개수는 상관없이 공백을 기준으로 리스트가 생성됨
list1= list(map(int, sys.stdin.readline().split()))
print('list1: ', list1)

# 활용 (2): 특정 자료형 입력한 값을 바로 리스트에 추가
list2= []
for i in range(2):
    list2.append(int(sys.stdin.readline()))

# 활용 (3): 특정 자료형 입력한 값을 바로 리스트에 추가(2)
list3= [ int(sys.stdin.readline()) for i in range(2)]

# 활용 (4): try-except을 이용하여 오류가 생길 때까지 계속 입력할 수 있음
while True:
    try:
        a,b = map(int, input().split())
        print(a+b)
    except EOFError:
        break