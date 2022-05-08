# 역순으로 선택정렬 시행하기

def reverse_selection_sort(a):
  n = len(a)
  for i in range(0, n - 1):
    max_idx = i
    for j in range(i + 1, n):
      if a[max_idx] < a[j]:
        max_idx = j
    a[i], a[max_idx] = a[max_idx], a[i]

d = [2, 4, 5, 1, 3]
reverse_selection_sort(d)
print(d)
