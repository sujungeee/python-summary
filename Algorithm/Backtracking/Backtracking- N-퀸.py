# 백트래킹
# : 유망 함수로 유망성을 판단하여 해가 될 가능성이 없는 분기(조건)를 배제한 후,
# 나머지 가능성 있는 분기에 대해 DFS를 수행하여 최적해나 모든 해를 찾음

# 백트래킹의 대표 유형
# 1) 부분집합 합
# 2) N-퀸

# 2) N-퀸
# : 체스의 퀸을 N*N 체스판에 N개 배치했을 때,
# 서로를 공격할 수 없는 위치에 놓을 수 있는 방법이 있는지 찾는 문제
# 2-1) 완전 탐색으로 풀기: 모든 가능성들을 탐색
# 2-2) 백트래킹으로 풀기: 답이 될 가능성만 탐색


# 유망 함수의 정의
# : 여왕이 추가될 때마다 행이나, 대각선 방향에 겹치는 여왕이 있으면 더 탐색하지 않기
# 상하좌우, 대각선에 퀸이 존재하지 않음을 확인해야 함

def nqueens(n, row, visited, diag1, diag2):
    ans= 0
    if row==n:
        return 1

    for col in range(n):
        if visited[col] or diag1[row+col] or diag2[row-col+n]:
            continue
        visited[col]= diag1[row+col]= diag2[row-col+n]= True
        ans+= nqueens(n, row+1, visited, diag1, diag2)
        visited[col]= diag1[row+col]= diag2[row-col+n] = False

    return ans

def solution(n):
    cnt= nqueens(n, 0, [False]*n, [False]*(n*2), [False]*(n*2))
    return cnt

print(solution(4))