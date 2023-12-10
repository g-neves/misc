def bubble_sort(arr):
    i = len(arr)
    while i > 0:
        is_sorted = True
        for j in range(i-1):
            if arr[j] > arr[j+1]:
                is_sorted = False 
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp 

        if is_sorted: # For early stop if it is already sorted
            break
        
        i -= 1

    return arr


if __name__ == "__main__":
    print(bubble_sort([1,3,7,4,2]))
    print(bubble_sort([1,3,7,4,2, 10, 1204, 13, 14, 13, 5]))

