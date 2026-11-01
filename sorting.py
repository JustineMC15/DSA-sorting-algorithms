def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    for p in range(n - 1): # p = pass number
        swapped = False # reset the flag at the start of each pass
        for i in range(n - 1 - p): # each pass skips the values already locked at the end
            comparisons += 1 # count every look at a pair
            if arr[i] > arr[i + 1]: # left is bigger > out of order
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                swaps += 1 # only count real swaps
                swapped = True
        if not swapped: # a pass with zero swaps means sorted leading to early exit
            break
    return comparisons, swaps

def selection_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    for i in range(n - 1): # i = the position being filled this pass
        min_idx = i # assume the smallest is at i
        for j in range(i + 1, n): # scan the unsorted part to the right of i
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j # remember WHERE the smallest is (no swap yet)
        if min_idx != i: # only swap if the smallest is not already at i
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
    return comparisons, swaps

def insertion_sort(arr):
    comparisons = 0
    shifts = 0
    for i in range(1, len(arr)): # arr[0] alone is already a sorted part
        current = arr[i] # the key: lifted out of the array
        j = i - 1 # j walks left through the sorted part
        while j >= 0 and current < arr[j]:
            comparisons += 1 # a comparison that succeeded
            arr[j + 1] = arr[j] # shift the bigger value one slot right
            shifts += 1
            j -= 1
        if j >= 0:
            comparisons += 1 # the comparison that failed and ended the loop
        arr[j + 1] = current # drop the key into the hole
    return comparisons, shifts
