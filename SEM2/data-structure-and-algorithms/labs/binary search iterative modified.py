def binary_search_iterative_modified(lst, item):
    low, high = 0, len(lst) - 1
    while True:
        guess = (low + high) // 2
        if high < low:
            break
        elif item == lst[guess]:
            return guess
        elif item < lst[guess]:
            high = guess - 1
        elif item > lst[guess]:
            low = guess + 1
    return guess + 1


print(binary_search_iterative_modified(lst, item))
