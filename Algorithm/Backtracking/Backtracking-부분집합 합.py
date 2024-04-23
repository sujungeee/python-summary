# 백트래킹
# : 유망 함수로 유망성을 판단하여 해가 될 가능성이 없는 분기(조건)를 배제한 후,
# 나머지 가능성 있는 분기에 대해 DFS를 수행하여 최적해나 모든 해를 찾음

# 백트래킹의 대표 유형
# 1) 부분집합 합
# 2) N-퀸

# 1) 부분집합 합
# : 1부터 N 까지 숫자 중 합이 10이 되는 조합 구하기
# 1-1) 완전 탐색으로 풀기: 모든 가능성들을 탐색
# 1-2) 백트래킹으로 풀기: 답이 될 가능성만 탐색


# 유망 함수의 정의
# : 현재 조합으로 합이 10이 되면 더 탐색하지 않기
# -> 더 탐색하면 10보다 커질 것이기 때문

# 제약 조건
# 1. 출력되는 숫자 조합은 오름차순으로 정렬되어 있어야 함
# 2. 같은 숫자는 한 번만 선택 가능

def setOfSum(N):
    result= []

    def backtrack(sum, selected_nums, start):
        if sum==10:
            result.append(selected_nums)
            return

        for i in range(start, N+1):
            if sum+i<=10:
                backtrack(sum+i, selected_nums+[i], i+1)

    backtrack(0, [], 1)

    return result

print(setOfSum(5))
print(setOfSum(2))
print(setOfSum(7))