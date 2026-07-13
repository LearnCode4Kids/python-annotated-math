"""题目：用列表表示的数字乘以一位数。

已知一个多位数列表和一个一位数列表。每个元素都是 0 到 9 的整数，按从左到右的顺序表示一个数。
例如 [1, 2, 3] 表示 123，[4] 表示 4。

要求：
1. 编写 multiply_lists(list1, list2)。
2. list2 只包含一位数。
3. 从个位开始逐位相乘，返回一个新列表。
4. 要考虑进位。
5. 不要修改原来的两个列表。

例子：
[1, 2, 3] 和 [4] 相乘，返回 [4, 9, 2]。
"""

a = [1, 2, 3]  # as a number
b = [4]  # as a number

def multiply_lists(list1, list2):
    """把一个列表表示的多位数乘以一位数，返回一个新的列表。

    Args:
        list1 (list[int]): 第一个列表，表示一个多位数。
        list2 (list[int]): 第二个列表，只表示一位数。

    Returns:
        list[int]: 考虑进位后的结果列表。
    """
    # Todo Begin
    pass
    # Todo End

c = multiply_lists(a, b)
print(c)  # Output: [4, 9, 2]

assert multiply_lists([1, 2, 3], [4]) == [4, 9, 2]
assert multiply_lists([0], [7]) == [0]
assert multiply_lists([2, 5], [3]) == [7, 5]
assert multiply_lists([9, 9], [9]) == [8, 9, 1]
assert multiply_lists([1, 0, 0], [5]) == [5, 0, 0]
