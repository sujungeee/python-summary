# 개념
# : 데이터의 빈도수를 세어 빈도수 배열에 저장하고 차례대로 출력

# 시간 복잡도
# (최선): O(N+K)
# (최악): O(N+K)

# 특징
#   - 데이터에 의존적이므로 항상 사용 가능한 것은 아님

def cnt_sort(strr):
    sortArr= ''
    frequencyArr= [0 for _ in range(26)]

    for s in strr:
        frequencyArr[ord(s)-97]+=1

    for i in range(26):
        sortArr+=chr(i+97)*frequencyArr[i]

    return sortArr

print(cnt_sort('hello'))
print(cnt_sort('algorithm'))