# [정리]
# ** yield 키워드
# - 호출한 쪽으로 프로그램 제어를 넘겨주는 키워드
# - 함수의 반환 값을 넘긴 후 함수를 종료하지 않고 중단된 상태로 유지

# * iterator(이터레이터)
# : iterable(tuple, range, set, list, str) 한 객체를 차례대로 꺼낼 수 있는 객체

a= [1, 2, 3]
print(type(iter(a))) # list_iterator
iter_a= iter(a)
print(next(iter_a)) # 1
print(next(iter_a)) # 2
print(next(iter_a)) # 3

# generator(제너레이터)
# : iterator를 생성해주는 함수, 함수 안에 yield 키워드를 사용함

# 제너레이터 특징
# - iterable한 순서가 지정됨  등등 ~

def test_generator():
    print('yield 1 전')
    yield 1
    print('yield 1과 2사이')
    yield 2
    print('yield 2와 3사이')
    yield 3
    print('yield 3 후')

gen= test_generator() 
print(type(gen)) # <class 'generator'>
print(next(gen)) # yield 1 전, 1
print(next(gen)) # yield 1과 2사이, 2
print(next(gen)) # yield 2와 3사이, 3
# print(next(gen)) # yield 3 후 # 오류: StopIteration