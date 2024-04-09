# 1. 리스트는 어떻게 만들고 사용할까?
list1= ['i', 1, 3]
print(list1) # ['i', 1, 3]
print(type(list1)) # <class 'list'>

# 배열 구현
    # 1. Array Module
import array as arr
array1= arr.array("i", [2,4,6])
print(array1) # array('i', [2, 4, 6])
print(type(array1)) # <class 'array.array'>

    # 2. Numpy
import numpy as np
array2= np.array(["numbers", 2,4,6])
print(array2) # ['numbers' '2' '4' '6']
print(type(array2)) # <class 'numpy.ndarray'>

# ***
# 리스트와 배열의 차이
# 1. 리스트- 같은 리스트 안에 여러 가지 데이터 타입이 가능하다.
#        - 같은 리스트에 object, string, integer를 합칠 수 있다.
#    배열- array 모듈의 경우 같은 배열 안에 여러 가지 데이터 타입이 가능하지 않다.
#       - numpy는 하나의 배열 안에 여러 가지 데이터 타입이 가능하다.

# 2. 리스트는 바로 수학 연산이 안된다.
#    배열은 바로 수학 연산이 가능하다.

# 리스트의 경우
list2= [2,4,6,8]
# division= list2/2 # 이 부분에서 오류!! -> for로 리스트의 요소에 하나씩 접근해야 함
for i in range(len(list2)):
    list2[i]= list2[i]/2
print(list2) # [1.0, 2.0, 3.0, 4.0]
print(type(list2)) # <class 'list'>

# 배열의 경우
array3= np.array([2,4,6,8])
division= array3/2
print(division) # [1. 2. 3. 4.]
print(type(division)) # <class 'numpy.ndarray'>

# 3. 리스트는 리스트 안에 리스트가 가능하다. 즉 중첩이 가능하다.
#    배열은 모든 원소가 같은 크기를 가져야 한다.
# array4= np.array([[1],[2,3]]) # 오류
array4= np.array([[0,1], [2,3]])
print(array4)
# [[0 1]
#  [2 3]]

# 언제 리스트, 배열을 쓰는게 좋을까?
# - 리스트가 좋은 경우
#    - 수학적 연산을 필요로 하지 않고, 적은 양의 아이템을 저장해야 할 때
#    - 배열보다 속도가 빠름
#    - 파이썬의 리스트를 기반으로 배열이 진행됨

# - 배열이 좋은 경우
#    - 매우 큰 양(amount)의 아이템을 저장하기 좋음, 효과적인 데이터 저장
#    - 각 아이템 간의 수학적 연산을 할 때 좋음
#    - 데이터 분석이나 데이터 사이언스는 주로 numpy에 의존

# ===============>
# 코테에서는 리스트가 좋겠다.


# 2.리스트의 인덱싱과 슬라이싱
a= [1,2,3,4]
    # 리스트의 인덱싱: 수학 연산도 가능
print(a[0]) # 1
print(a[0]+a[2]) # 4
print(a[-1]) # 3

a= [1,2,3, ['a', 'b', 'c']]
print(a[0]) # 1
print(a[-1]) # ['a', 'b', 'c']
print(a[3]) # ['a', 'b', 'c']
print(a[-1][1]) # 'b'
print(a[-1][2]) # 'c'

    # 리스트의 슬라이싱
a= [1,2,3,4,5]
print(a[0:2]) # [1, 2]

a= '12345'
print(a[0:2]) # '12'

a= [1,2,3,4,5]
b= a[:2]
c= a[2:]
print(b) # [1, 2]
print(c) # [3, 4, 5]
print(a[-2:-1]) # [4]

# 3. 리스트 연산하기
a= [1, 2, 3]
b= [4, 5, 6]
    # 리스트 더하기(+)
print(a+b) # [1, 2, 3, 4, 5, 6]

    # 리스트 반복하기(*)
print(a*3) # [1, 2, 3, 1, 2, 3, 1, 2, 3]

    # 리스트 길이 구하기
print(len(a)) # 3

# 4. 리스트의 수정과 삭제
a= [1, 2, 3]
    # 리스트의 값 수정하기
a[2]= 4
print(a) # [1, 2, 4]

    # del 함수를 사용해 리스트 요소 삭제하기
del a[1]
print(a) # [1, 4]

a= [1, 2, 3, 4, 5]
del a[2:]
print(a) # [1, 2]

# 5. 리스트 관련 함수
a= [1, 2, 3]
    # 리스트에 요소 추가하기 - append
a.append(4)
print(a) # [1, 2, 3, 4]
a.append([5, 6])
print(a) # [1, 2, 3, 4, [5, 6]]

    # 리스트 정렬 - sort
a= [1, 4, 3, 2]
a.sort()
print(a) # [1, 2, 3, 4]

a= ['a', 'c', 'b']
a.sort()
print(a) # ['a', 'b', 'c']

    # 리스트 뒤집기 - reverse
a= ['a', 'c', 'b']
a.reverse()
print(a) # ['b', 'c', 'a']

    # 인덱스 반환 - index
a= [1, 2, 3]
print(a.index(3)) # 2
print(a.index(1)) # 0
# print(a.index(100)) # 오류!!

    # 리스트에 요소 삽입 - insert
a= [1, 2, 3]
a.insert(0, 4)
print(a) # [4, 1, 2, 3]

    # 리스트 요소 제거 - remove
a= [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a) # [1, 2, 1, 2, 3]

    # 리스트 요소 끄집어 내기 - pop
a= [1, 2, 3]
a.pop()
print(a) # [1, 2]

a= [1, 2, 3]
a.pop(1)
print(a) # [1, 3]

    # 리스트에 포함된 요소 x의 개수 세기 - count
a= [1, 2, 3, 1]
print(a.count(1)) # 2

    # 리스트 확장 - extend
a= [1, 2, 3]
a.extend([4, 5])
print(a) # [1, 2, 3, 4, 5]
b= [6, 7]
a.extend(b)
print(a) # [1, 2, 3, 4, 5, 6, 7]