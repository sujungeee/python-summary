# 240612- 공부(1)

# 키 값을 기준으로 딕셔너리를 정렬: sorted(path.items())
# 정렬된 결과를 딕셔너리로 변환: dict(sorted(path.items())
# 딕셔너리의 값을 기준으로 정렬: sorted(path.items(), key= lambda item:item[1])

graph= {'A': {'B':9, 'C':3}, 'B':{'A':5}, 'C':{'B':1}}

for k, v in graph.items():
    print(k) # A, B, C
    print(dict(v.items())) # {'B':9, 'C':3}, {'A':5}, {'B':1}

# 딕셔너리 안의 딕셔너리의 값을 기준으로 정렬
sorted_graph= {k: dict(sorted(v.items(), key= lambda x: x[1])) for k, v in graph.items()}
print(sorted_graph) # {'A': {'C': 3, 'B': 9}, 'B': {'A': 5}, 'C': {'B': 1}}

# 각 키에 대한 내부 딕셔너리의 최소값을 기준으로 외부 딕셔너리 정렬
sorted_graph_by_value= dict(sorted(graph.items(), key= lambda item: min(item[1].values())))
print(sorted_graph_by_value) # {'C': {'B': 1}, 'A': {'B': 9, 'C': 3}, 'B': {'A': 5}}

# graph.items(): (키, 값) 쌍의 튜플 리스트
# -> dict_items([('A', {'B': 9, 'C': 3}), ('B', {'A': 5}), ('C', {'B': 1})])

# sorted를 이용하여 내부 딕셔너리의 최소값을 기준으로 정렬
# -> [('C', {'B': 1}), ('A', {'C': 3, 'B': 9}), ('B', {'A': 5})]

# 딕셔너리로 다시 변환
# -> {'C': {'B': 1}, 'A': {'B': 9, 'C': 3}, 'B': {'A': 5}}