import random
# 개념
# 정렬되지 않은 영역에서 현재 인덱스 값을 왼쪽에 있는 모든 값과 차례로 비교하여,
# 값이 작으면 자리를 교환
# (~ 마지막 데이터가 올바른 위치를 찾을 때까지)

# 시간 복잡도
# (최선): O(N)
# (최악): O(N^2)

# 특징
#   - 데이터가 거의 정렬되어 있을 때는 최고의 성능을 발휘

# 과정
def insertion_sort(arr):
    for i in range(1, len(arr)):
        print(f'시작 인덱스 {i}')
        print(arr)

        while i>0 and arr[i] < arr[i-1]:
            arr[i], arr[i-1]= arr[i-1], arr[i]
            i-=1
            print(arr)

    return arr

datas= []
for _ in range(10):
    datas.append(random.randrange(15))

print('정렬 전: ', datas)
print()
print('정렬 후 : ', insertion_sort(datas))