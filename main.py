from sorting import bubble_sort, selection_sort, insertion_sort

# (name, input) pairs: the minimum test cases from the activity
test_cases = [
    ("A. Random",        [29, 10, 14, 37, 13, 5, 22]),
    ("B. Already sorted", [1, 2, 3, 4, 5, 6, 7]),
    ("C. Reverse sorted", [7, 6, 5, 4, 3, 2, 1]),
    ("D. Duplicates",    [4, 2, 4, 1, 2, 3, 1]),
    ("E1. Empty",        []),
    ("E2. One element",  [42]),
    ("E3. Two elements", [2, 1]),
    ("F. Nearly Sorted", [1, 2, 4, 3, 5, 6, 7])
]

# (name, function) pairs
algorithms = [
    ("Bubble",    bubble_sort),
    ("Selection", selection_sort),
    ("Insertion", insertion_sort),
]

for case_name, data in test_cases:
    print(f"{case_name}: input = {data}")
    for algo_name, func in algorithms:
        arr = data[:]                   # fresh copy: the sorts change the list in place
        comparisons, moves = func(arr)
        print(f"  {algo_name:<9} -> {arr}  comparisons={comparisons}, swaps/shifts={moves}")
    print()
