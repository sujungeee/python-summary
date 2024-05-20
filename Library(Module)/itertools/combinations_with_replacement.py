from itertools import combinations_with_replacement
from collections import Counter

arr= [1, 2, 3]

for i in combinations_with_replacement(arr, 5):
    print(i, end= ' ')
    print(Counter(i))