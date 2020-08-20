def bute_force_search(array, value):
    steps = 0
    for element in array:
        steps += 1
        if element == value:
            return value, steps
    return None, steps

def linear_search(array, value):
    step = 0 
    for element in array:
        step += 1
        if element == value:
            return value, step
        elif element > value:
            break
    return None, step

# 정렬된 배열
data = [3, 17, 75, 80, 202]

linear_search_r, linear_search_steps = linear_search(data, 22)
print(linear_search_r, linear_search_steps)

bute_force_search_r, bute_force_search_steps = bute_force_search(data, 22)
print(bute_force_search_r, bute_force_search_steps)
