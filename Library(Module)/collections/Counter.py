from collections import Counter

# 1. 개념
score= [1, 2, 2, 1, 1, 3, 3, 3, 3, 3, 3, 3, 4, 4]
c1= Counter(score)
# print(c1) # Counter({3: 7, 1: 3, 2: 2, 4: 2})

str1= 'Hello world!'
c2= Counter(str1)
# print(c2) # Counter({'l': 3, 'o': 2, 'H': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1, '!': 1})




# 2. Counter를 딕셔너리처럼 사용하기
# : 키 -> 원소(Counter 대상)
# : 값 -> 빈도 수

# 2-1
# print(c2['o']) # 2
# print(c2['l']) # 3

# 2-2
c2['o'] += 100
c2['l'] -= 2
# print(c2['o']) # 102
# print(c2['l']) # 1

# 2-3
# print('o' in c2) # True
# print('k' in c2) # False




# 3. most_common()!!!!!
# : 데이터의 개수, 즉 빈도수가 큰 순서대로 정렬된 배열을 리턴하는 메소드

str2= 'Heeeello Wworld!'
c3= Counter(str2)

# print(c3.most_common()) # [('e', 4), ('l', 3), ('o', 2), ('H', 1), (' ', 1), ('W', 1), ('w', 1), ('r', 1), ('d', 1), ('!', 1)]

# >2 인 빈도수
# print(c3.most_common(2)) # [('e', 4), ('l', 3)]

# 가장 큰 빈도수를 가지는 원소
print(c3.most_common()[0][0]) # e
# 가장 큰 빈도수
print(c3.most_common()[0][1]) # 4


# 4. 산술 연산자 활용

counter1= Counter(['A', 'A', 'B'])
counter2= Counter(['A', 'B', 'C'])

# print(counter1 + counter2) # Counter({'A': 3, 'B': 2, 'C': 1})
# print(counter1 - counter2) # Counter({'A': 1})
# 빈도수가 0 이하인 counter는 제외됨!!