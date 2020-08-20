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
