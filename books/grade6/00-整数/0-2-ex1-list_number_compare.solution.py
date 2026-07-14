"""题目：比较两个用列表表示的整数大小。

已知两个长度不一定相等的列表。每个元素都是 0 到 9 的整数，按从左到右的顺序表示一个数。
例如 [3, 5, 6] 表示 356，[4, 7] 表示 47。

要求：
1. 编写 compare_lists(list1, list2)。
2. 如果 list1 表示的数更大，返回 1。
3. 如果两个数相等，返回 0。
4. 如果 list1 表示的数更小，返回 -1。
5. 不要修改原来的两个列表。

例子：
[3, 5, 6] 比 [4, 7] 大，返回 1。
"""

a = [3, 5, 6]  # as a number
b = [4, 7]  # as a number

def compare_lists(list1, list2):
    """比较两个列表表示的整数大小。

    Args:
        list1 (list[int]): 第一个列表，表示一个整数。
        list2 (list[int]): 第二个列表，表示一个整数。

    Returns:
        int: list1 更大返回 1，相等返回 0，更小返回 -1。
    """
    left = list1[:]
    right = list2[:]

    while len(left) > 1 and left[0] == 0:
        left.pop(0)
    while len(right) > 1 and right[0] == 0:
        right.pop(0)

    if len(left) > len(right):
        return 1
    if len(left) < len(right):
        return -1

    for index in range(len(left)):
        if left[index] > right[index]:
            return 1
        if left[index] < right[index]:
            return -1

    return 0

c = compare_lists(a, b)
print(c)  # Output: 1

assert compare_lists([3, 5, 6], [4, 7]) == 1
assert compare_lists([1, 2, 3], [1, 2, 3]) == 0
assert compare_lists([9, 9], [1, 0, 0]) == -1
assert compare_lists([0, 0, 5], [5]) == 0
assert compare_lists([1, 0, 0, 0], [9, 9, 9]) == 1
