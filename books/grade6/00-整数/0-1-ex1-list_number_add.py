"""题目：用列表表示的数字相加。

已知两个长度相等的列表。每个元素都是 0 到 9 的整数，按从左到右的顺序表示一个数。
例如 [3, 5, 6] 表示 356，[4, 7, 8] 表示 478。

要求：
1. 编写 add_lists(list1, list2)。
2. 按对应位置相加，返回一个新列表。
3. 要考虑进位。
4. 不要修改原来的两个列表。

例子：
[3, 5, 6] 和 [4, 7, 8] 相加，返回 [8, 3, 4]。
"""

a = [3, 5, 6]  # as a number
b = [4, 7, 8]  # as a number

def add_lists(list1, list2):
    """把两个列表表示的数相加，返回一个新的列表。

    Args:
        list1 (list[int]): 第一个列表，表示一个数。
        list2 (list[int]): 第二个列表，表示一个数。

    Returns:
        list[int]: 考虑进位后的结果列表。
    """
    # Todo Begin
    pass
    # Todo End

c = add_lists(a, b)
print(c)  # Output: [8, 3, 4]

assert add_lists([3, 5, 6], [4, 7, 8]) == [8, 3, 4]
assert add_lists([0], [0]) == [0]
assert add_lists([1, 2, 3], [0, 0, 0]) == [1, 2, 3]
assert add_lists([9, 9], [0, 1]) == [1, 0, 0]