"""题目：用插入排序给列表排序。

已知一个由整数组成的列表。请把它从小到大排列。
例如 [5, 1, 4, 2, 0] 排序后是 [0, 1, 2, 4, 5]。

"""

data = [5, 1, 4, 2, 0]


def insertion_sort(numbers):
    """用插入排序把列表从小到大排列。

    Args:
        numbers (list[int]): 需要排序的整数列表。

    Returns:
        list[int]: 从小到大排好序的新列表。
    """
    # Todo Begin
    numbers = numbers.copy()

    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1

        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j -= 1

        numbers[j + 1] = key

    return numbers
    # Todo End


sorted_data = insertion_sort(data)
print(sorted_data)  # Output: [0, 1, 2, 4, 5]

assert insertion_sort([5, 1, 4, 2, 0]) == [0, 1, 2, 4, 5]
assert insertion_sort([3, 2, 0, 1]) == [0, 1, 2, 3]
assert insertion_sort([0, -3, 2, -1]) == [-3, -1, 0, 2]
assert insertion_sort([2, 2, 1, 3]) == [1, 2, 2, 3]
assert insertion_sort([]) == []
assert insertion_sort([7]) == [7]

original = [3, 1, 2]
assert insertion_sort(original) == [1, 2, 3]
assert original == [3, 1, 2]
