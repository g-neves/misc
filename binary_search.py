def binary_search(arr, val):
    low, high = 0, len(arr)

    while True:
        pos = low + (high - low)//2
        if arr[pos] == val:
            return pos
        elif arr[pos] < val:
            low = pos 
        else:
            high = pos

        if high - low == 1: # If we don't find the match at the end of iteration
            return -1
