"""题目：用列表表示的数字相减。

已知两个长度不一定相等的列表。每个元素都是 0 到 9 的整数，按从左到右的顺序表示一个数。
例如 [5, 0, 2] 表示 502，[7, 8] 表示 78。

要求：
1. 编写 subtract_lists(list1, list2)。
2. 本题只考虑 list1 表示的数大于或等于 list2 表示的数。
3. 从个位开始逐位相减。
4. 如果不够减，就向前一位借 1。本题用 carrier 表示“上一位借走的 1”。
5. 不要修改原来的两个列表。

例子：
[5, 0, 2] 减 [7, 8]，返回 [4, 2, 4]。
"""

a = [5, 0, 2]  # as a number
b = [7, 8]  # as a number

def subtract_lists(list1, list2):
    """把两个列表表示的整数相减，返回一个新的列表。

    Args:
        list1 (list[int]): 被减数列表，表示一个整数。
        list2 (list[int]): 减数列表，表示一个整数。

    Returns:
        list[int]: list1 - list2 的结果列表。
    """
    # Todo Begin
    pass
    # Todo End

c = subtract_lists(a, b)
print(c)  # Output: [4, 2, 4]

assert subtract_lists([5, 0, 2], [7, 8]) == [4, 2, 4]
assert subtract_lists([1, 0, 0], [1]) == [9, 9]
assert subtract_lists([1, 2, 3], [1, 2, 3]) == [0]
assert subtract_lists([0, 0, 5], [5]) == [0]
assert subtract_lists([9, 0, 0], [4, 5, 6]) == [4, 4, 4]
