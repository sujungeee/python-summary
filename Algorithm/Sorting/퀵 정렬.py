# 개념 !!!!(분할 정복 알고리즘, 재귀 알고리즘)!!!!
# : pivot을 중심으로 파티셔닝을 하여 분할 정복하는 알고리즘

# 시간 복잡도
# (최선): O(NlogN)
# (최악): O(N^2)

# 특징
#   - 병합 정렬처럼 분할 정복 알고리즘이지만 추가 메모리 공간이 필요 없다.
#   - 불안정 정렬이다.
#   - 정렬된 배열일 때는 수행 시간이 늘어나지만 빠르다.

# 전체 과정
# 1) 분할
#   - 주어진 배열을 파티셔닝한다.
#   - 피벗의 왼쪽 리스트와 오른쪽 리스트에 다시 퀵 정렬을 한다.
#       -> 더 이상 나누는게 불가능할 때까지 반복
# 2) 정복
#   - 퀵 정렬을 한 번 호출할 때마다, 최소 하나 이상의 숫자가 정렬된다.
#   - 길이가 0이나 1이면 이미 주어진 리스트가 정렬된 상태이므로 리스트 반환
# 3) 조합
#   - 피벗의 왼쪽과 오른쪽을 합치면 전체 리스트가 정렬된다.

# 재귀 이용
def quick_sort(arr):
    if len(arr)<=1:
        return arr

    pivot= arr[0]
    tail= arr[1:]

    left_side= [x for x in tail if x <= pivot]
    right_side= [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort([2, 4, 1, 8, 6, 5, 7, 3, 9]))