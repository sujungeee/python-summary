# functools 라이브러리
# : 함수 프로그래밍 도구들을 제공하는 모듈
# - 고차함수를 다루기 위한 다양한 유틸리티를 포함한다.
# - 함수 호출의 동작을 수정하거나 새로운 함수로 감싼다.

# 1. functools.reduce()
# : 누적함수- 시퀀스의 원소들에 누적된 연산을 적용하여 단일 결과를 반환
from functools import reduce

numbers= [1, 2, 3, 4]
result= reduce(lambda x,y: x+y, numbers)
print(result) # 10

# 2. functools.partial()
# : 함수를 부분적으로 적용하여 새로운 함수를 생성
# , 특정 인수를 고정하여 나중에 더 적은 인수를 사용해 호출할 수 있음
from functools import partial

def multiply(x, y):
    return x*y

double= partial(multiply, 2)
print(double(5)) # 10

# 3. functools.lru_cache()
# : 함수의 결과를 캐시하여, 동일한 인수로 호출될 때 계산을 생략하고 캐시된 결과를 반환
# -> 나중에 메모이제이션에서 써보기(근데 별로 안쓰일 것 같긴 함)
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n<2:
        return n
    return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(6)) # 0, 1, 1, 2, 3, 5, 8

# 4. functools.cmp_to_key()
# : 비교 함수를 키 함수로 변환함
# - 정렬 함수에서 사용자 정의 비교 함수를 사용할 수 있음
from functools import cmp_to_key

def compare(x, y):
    return (x>y)-(x<y) # 양수이면 y가 먼저 삽입

sorted_numbers= sorted([5, 2, 4, 1, 3], key= cmp_to_key(compare))
print(sorted_numbers) # [1, 2, 3, 4, 5]

# 5. functools.total_ordering()
# : 클래스에 최소한의 비교 연산자만 정의해도 나머지 연산자들을 자동으로 제공해줌
from functools import total_ordering

@total_ordering
class Person:
    def __init__(self, name, age):
        self.name= name
        self.age= age

    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return self.age < other.age

    def __gt__(self, other):
        return self.age > other.age

p1= Person('Alice', 30)
p2= Person('Bob', 25)

print(p1>p2) # True