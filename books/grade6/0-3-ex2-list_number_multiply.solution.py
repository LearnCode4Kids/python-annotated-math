"""题目：用列表表示的多位数相乘。

已知两个列表。每个元素都是 0 到 9 的整数，按从左到右的顺序表示一个数。
例如 [1, 2, 3] 表示 123，[4, 5] 表示 45。

要求：
1. 编写 multiply_lists(list1, list2)。
2. 使用竖式乘法的想法：先用 list1 乘 list2 的每一位。
3. 每往左一位，部分积后面要多补一个 0。
4. 把所有部分积相加，返回一个新列表。
5. 要考虑进位。
6. 不要修改原来的两个列表。

例子：
[1, 2, 3] 和 [4, 5] 相乘，返回 [5, 5, 3, 5]。
"""

a = [1, 2, 3]  # as a number
b = [4, 5]  # as a number

def remove_leading_zeros(number):
    """去掉结果前面多余的 0，但保留数字 0 自己。"""
    while len(number) > 1 and number[0] == 0:
        number.pop(0)
    return number

def multiply_by_one_digit(number, one_digit):
    """把一个列表表示的多位数乘以一位数，返回一个新的列表。"""
    result = []
    carry = 0

    for index in range(len(number) - 1, -1, -1):
        digit_product = number[index] * one_digit + carry
        result.insert(0, digit_product % 10)
        carry = digit_product // 10

    while carry > 0:
        result.insert(0, carry % 10)
        carry = carry // 10

    return remove_leading_zeros(result)

def add_lists(list1, list2):
    """把两个列表表示的数相加，返回一个新的列表。"""
    max_len = max(len(list1), len(list2))
    left = [0] * (max_len - len(list1)) + list1
    right = [0] * (max_len - len(list2)) + list2

    result = []
    carry = 0

    for index in range(max_len - 1, -1, -1):
        digit_sum = left[index] + right[index] + carry
        result.insert(0, digit_sum % 10)
        carry = digit_sum // 10

    if carry > 0:
        result.insert(0, carry)

    return remove_leading_zeros(result)

def multiply_lists(list1, list2):
    """把两个列表表示的多位数相乘，返回一个新的列表。

    Args:
        list1 (list[int]): 第一个列表，表示一个多位数。
        list2 (list[int]): 第二个列表，表示一个多位数。

    Returns:
        list[int]: 考虑进位后的结果列表。
    """
    result = [0]
    zeros_count = 0

    for index in range(len(list2) - 1, -1, -1):
        one_digit = list2[index]
        partial_result = multiply_by_one_digit(list1, one_digit)

        if partial_result != [0]:
            partial_result = partial_result + [0] * zeros_count

        result = add_lists(result, partial_result)
        zeros_count = zeros_count + 1

    return remove_leading_zeros(result)

c = multiply_lists(a, b)
print(c)  # Output: [5, 5, 3, 5]

assert multiply_lists([1, 2, 3], [4, 5]) == [5, 5, 3, 5]
assert multiply_lists([1, 2], [3, 4]) == [4, 0, 8]
assert multiply_lists([9, 9], [9, 9]) == [9, 8, 0, 1]
assert multiply_lists([0], [5, 6]) == [0]
assert multiply_lists([1, 0, 0], [2, 0]) == [2, 0, 0, 0]
