# 제너레이터
# 

# 제너레이터를 이용한 순열
def permutation(arr, r):
    for i in range(len(arr)):
        if r==1:
            yield [arr[i]]
        else:
            for next in permutation(arr[:i]+arr[i+1:], r-1):
                yield [arr[i]] + next

# 제너레이터를 이용한 조합
def combination(arr, r):
    for i in range(len(arr)):
        if r==1:
            yield [arr[i]]
        else:
            for next in combination(arr[i+1:], r-1):
                yield [arr[i]] + next

arr= [1, 2, 3, 4]
r= 2
print(list(permutation(arr, r)))
print(list(combination(arr, r)))