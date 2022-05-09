
# 재귀 X
def binary_search1(element, some_list):
    start_index = 0
    end_index = len(some_list) - 1
    
    while start_index <= end_index:
        midpoint = (start_index + end_index) // 2
        if some_list[midpoint] == element:
            return midpoint
        elif some_list[midpoint] > element:
            end_index = midpoint - 1
        else:
            start_index = midpoint + 1
    return None

print(binary_search1(2, [2, 3, 5, 7, 11]))
print(binary_search1(0, [2, 3, 5, 7, 11]))
print(binary_search1(5, [2, 3, 5, 7, 11]))
print(binary_search1(3, [2, 3, 5, 7, 11]))
print(binary_search1(11, [2, 3, 5, 7, 11]))
print()

# 재귀 O
def binary_search2(element, some_list, start_index = 0, end_index = None):
    # end_index가 따로 주어지지 않은 경우에는 리스트의 마지막 인덱스
    if end_index == None:
        end_index = len(some_list) - 1

    # 코드를 작성하세요.
    mid = (start_index + end_index) // 2
    if start_index > end_index:
        return None
    elif some_list[mid] == element:
        return mid
    elif some_list[mid] > element:
        return binary_search2(element, some_list, start_index, mid - 1)
    else:
        return binary_search2(element, some_list, mid + 1, end_index)

print(binary_search2(2, [2, 3, 5, 7, 11]))
print(binary_search2(0, [2, 3, 5, 7, 11]))
print(binary_search2(5, [2, 3, 5, 7, 11]))
print(binary_search2(3, [2, 3, 5, 7, 11]))
print(binary_search2(11, [2, 3, 5, 7, 11]))
