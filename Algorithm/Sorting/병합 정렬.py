# 개념 !!!!(분할 정복 알고리즘, 재귀 알고리즘)!!!!
# : 배열을 작은 하위 배열로 나눠서 정렬한 후에 다시 합병하는 알고리즘

# 시간 복잡도
# (최선): O(NlogN)
# (최악): O(NlogN)
# 공간 복잡도: O(N) -> 분할할 배열을 저장해야 함

# 특징
#   - 안정적인 성능으로 정렬할 수 있음
#   - 병합 과정에서 추가적인 메모리가 필요

# 전체 과정
# 1) 부분 배열의 길이가 1이 될 때까지 분할
# 2) 분할한 부분 배열을 정렬
# 3) 정렬한 배열들을 하나로 합쳐서 정렬 결과를 출력

# 재귀(recursion)를 이용해서 병합 정렬 구현
# 분할 정복 알고리즘은 while을 이용하면 됨(나중에 하고 싶을 때 while로 구현해보기)

def merge(arr, low, mid, high):
    cpArr= arr[:]
    idx1= low
    idx2= mid+1
    while idx1<=mid and idx2<=high:
        if cpArr[idx1] <= cpArr[idx2]:
            arr[low]= cpArr[idx1]
            idx1+=1
        else:
            arr[low]= cpArr[idx2]
            idx2+=1
        low+=1

    # low: 현재까지 정렬된 개수
    for i in range(idx1, mid+1): # 오른쪽 부분 배열이 모두 다 쓰인 경우
        arr[low]= cpArr[i]
        low+=1
    for i in range(idx2, high+1): # 왼쪽 부분 배열이 모두 다 쓰인 경우
        arr[low]= cpArr[i]
        low+=1

def merge_sort1(arr):
    def merge_sort2(left, right):
        if left==right: # 더 이상 부분 배열을 쪼갤 수 없을 때(데이터가 1개일 때)
            return

        # 가운데 인덱스의 뒤 쪽에서 분할하기
        mid= (left+right)//2
        merge_sort2(left, mid)
        merge_sort2(mid+1, right)
        merge(arr, left, mid, right)

    merge_sort2(0, len(arr)-1)

    return datas

datas= [24, 26, 2, 16, 32, 31, 25]
print('정렬 전: ', datas)
print()
print('정렬 후: ', merge_sort1(datas))