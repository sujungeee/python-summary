# 1. 딕셔너리란?

# 2. 딕셔너리는 어떻게 만들까?
dic= {}
dic= {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
dic= {'a': [1,2,3]}

# 3. 딕셔너리 쌍 추가, 삭제하기
    # 딕셔너리 쌍 추가하기
a= {1:'a'}
a[2]= 'b'
print(a) # {1: 'a', 2: 'b'}

    # 딕셔너리 요소 삭제하기
del a[1]
print(a) # {2: 'b'}

# 4. 딕셔너리를 사용하는 방법
    # 딕셔너리에서 Key를 사용해 Value 얻기
print(a[2])

    # 딕셔너리 만들 때 주의할 사항
    #   - key는 중복되면 안됨!

# 5. 딕셔너리 관련 함수
    # Key 리스트 만들기 - keys
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.keys()) # dict_keys(['name', 'phone', 'birth'])
print(list(a.keys())) # ['name', 'phone', 'birth']

    # Value 리스트 만들기 - values
print(a.values()) # dict_values(['pey', '010-9999-1234', '1118'])
print(list(a.values())) # ['pey', '010-9999-1234', '1118']

    # Key, Value 쌍 얻기 - items
print(a.items()) # dict_items([('name', 'pey'), ('phone', '010-9999-1234'), ('birth', '1118')])

    # Key: Value 쌍 모두 지우기 - clear
print(a.clear()) # None

    # Key로 Value 얻기 - get
a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.get('name')) # pey
print(a.get('phone')) # 010-9999-1234
print(a.get('nokey')) # None
# print(a['nokey']) # 오류

    # 해당 Key가 딕셔너리 안에 있는지 조사하기 - in
print('name' in a) # True
print('email' in a) # False