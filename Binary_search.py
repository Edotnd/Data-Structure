def binary_search(array, value):
    steps = 0 
    # 최초의 상한선은 배열의 첫 번째 인덱스, 하한선은 배열의 마지막 인덱스
    lower_bound = 0
    upper_bound = len(array)-1

    while lower_bound <= upper_bound:
        steps += 1
        midpoint = int((upper_bound + lower_bound)/2) # 중간지점 인덱스 계산
        value_at_midpoint = array[midpoint]

        if value < value_at_midpoint:
            upper_bound = midpoint - 1
        elif value > value_at_midpoint:
            lower_bound = midpoint + 1
        elif value == value_at_midpoint:
            return midpoint, steps

    return None, steps

# 정렬된 배열에서 이진검색
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

binary_search_r, binary_search_steps = binary_search(data, 5)
print(binary_search_r, binary_search_steps)