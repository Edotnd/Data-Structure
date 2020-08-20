def bute_force_search(array, value):
    steps = 0
    for element in array:
        steps += 1
        if element == value:
            return value, steps
    return None, steps
