def merge_sort(arr):
    length = len(arr)
    # If length is equal to or less than 1, return the array.
    # Avoids infinite recursion
    if length <= 1:
        return arr

    mid = length // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)
    
def merge(left, right):
    output = []
    i = j = 0
    # While both arrays have elements
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1

    output.extend(left[i:])
    output.extend(right[j:])

    return output

def main():
    unsorted_input = [7, 23, 4, 42, 15, 38, 11, 49, 19, 31, 26, 50]
    sorted = merge_sort(unsorted_input)
    print(sorted)

    unsorted_input = [14, 33, 8, 47]
    sorted = merge_sort(unsorted_input)
    print(sorted)

    empty = []
    sorted = merge_sort(empty)
    print(sorted)


main()
