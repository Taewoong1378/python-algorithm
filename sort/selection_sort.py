# 삽입 정렬
# 입력: 리스트 a
# 출력: 없음(입력으로 주어진 a가 정렬됨)

def selection_sort(a):
	n = len(a)
	for i in range(0, n - 1):
		# i번 위치부터 끝까지 자료 값 중 최솟값의 위치를 찾음
		min_idx = i
		for j in range(i + 1, n):
			if a[j] < a[min_idx]:
				min_idx = j
		
		# 찾은 최솟값을 i번 위치로
		a[i], a[min_idx] = a[min_idx], a[i]


d = [2, 4, 5, 1, 3]
selection_sort(d)
print(d)

# 결과 : [1, 2, 3, 4, 5]
