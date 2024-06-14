# 1. 순열
print('순열')
from itertools import permutations

arr= [1, 2, 3]
print(list(permutations(arr, 3))) # [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
# permutations의 두 번째 인수는 len(arr)을 초과할 수 없음

# 2. 중복 순열 (데카르트의 곱)
print('중복 순열')
from itertools import product

# 2-1. arr이 단순 배열일 때
arr= ['+', '-']
print(list(product(arr, repeat= 3))) # [('+', '+', '+'), ('+', '+', '-'), ('+', '-', '+'), ('+', '-', '-'), ('-', '+', '+'), ('-', '+', '-'), ('-', '-', '+'), ('-', '-', '-')]
# arr로 중복되어 순열을 만들 수 있음
# repeat는 len(arr)을 초과할 수 있음

# 2-2. arr이 튜플 형태일 때
arr= [(1, -1), (2, -2)]
print(list(product(*arr))) # [(1, 2), (1, -2), (-1, 2), (-1, -2)]
# 튜플 하나가 하나의 항으로 작용되어, 튜플 내의 값을 하나씩 선택할 수 있음

# 2-2-1. 활용
print(list(map(sum, product(*arr)))) # [3, -1, 1, -3]
# 위 리스트 내의 튜플을 더한 값들을 리스트에 저장할 수 있음




# 조합
print('조합')
from itertools import combinations

arr= [1, 2, 3, 4]
print(list(combinations(arr, 2))) # [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]


# 중복 조합
print('중복 조합')
from itertools import combinations_with_replacement

arr= [1, 3, 5]
print(list(combinations_with_replacement(arr, 4))) # [(1, 1, 1, 1), (1, 1, 1, 3), (1, 1, 1, 5), (1, 1, 3, 3), (1, 1, 3, 5), (1, 1, 5, 5), (1, 3, 3, 3), (1, 3, 3, 5), (1, 3, 5, 5), (1, 5, 5, 5), (3, 3, 3, 3), (3, 3, 3, 5), (3, 3, 5, 5), (3, 5, 5, 5), (5, 5, 5, 5)]


# ------- 결 론 -------
# 중복 순열과 조합은 두 번째 인자가 len(arr)을 초과할 수 있지만,
# 그냥 순열과 조합은 두 번째 인자가 len(arr)을 초과하지 못함