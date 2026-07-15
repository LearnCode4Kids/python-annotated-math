"""题目：用列表模仿竖式除法。

已知两个列表。每个元素都是 0 到 9 的整数，按从左到右的顺序表示一个数。
例如 [1, 2, 3, 4] 表示 1234，[1, 2] 表示 12。

要求：
1. 编写 divide_lists(list1, list2)。
2. list2 表示的数不能是 0。
3. 从左到右处理 list1，每次把下一位“落下来”。
4. 每一步用减法求出当前这一位商。
5. 返回两个新列表：商列表和余数列表。
6. 不要修改原来的两个列表。

例子：
[1, 2, 3, 4] 除以 [1, 2]，返回 ([1, 0, 2], [1, 0])。
因为 1234 ÷ 12 = 102 余 10。
"""

a = [1, 2, 3, 4]  # as a number
b = [1, 2]  # as a number

def remove_leading_zeros(number):
    """去掉前面多余的 0，但保留数字 0 自己。"""
    while len(number) > 1 and number[0] == 0:
        number.pop(0)
    return number

def divide_lists(list1, list2):
    """把两个列表表示的整数相除，返回商列表和余数列表。

    Args:
        list1 (list[int]): 被除数列表，表示一个整数。
        list2 (list[int]): 除数列表，表示一个非零整数。

    Returns:
        tuple[list[int], list[int]]: 商列表和余数列表。
    """
    if compare_lists(list2, [0]) == 0:
        raise ValueError("除数不能是 0")

    q = []  # q 是 quotient 的缩写，表示商。
    r = [0]  # r 是 remainder 的缩写，表示当前余数。

    for d in list1:  # d 是 digit 的缩写，表示当前落下来的一位数字。
        r.append(d)
        remove_leading_zeros(r)

        q_d = 0  # q_d 是 quotient digit 的缩写，表示当前这一位的商。
        while compare_lists(r, list2) >= 0:
            r = subtract_lists(r, list2)
            q_d += 1

        q.append(q_d)

    return remove_leading_zeros(q), r

def subtract_lists(list1, list2):
    """把两个列表表示的整数相减，返回一个新的列表。"""
    result = []
    borrow = 0
    i = len(list1) - 1
    j = len(list2) - 1

    while i >= 0:
        top_d = list1[i] - borrow
        bottom_d = list2[j] if j >= 0 else 0

        if top_d < bottom_d:
            top_d += 10
            borrow = 1
        else:
            borrow = 0

        result.insert(0, top_d - bottom_d)
        i -= 1
        j -= 1

    return remove_leading_zeros(result)

def compare_lists(list1, list2):
    """比较两个列表表示的整数大小。"""
    left = remove_leading_zeros(list1[:])
    right = remove_leading_zeros(list2[:])

    if len(left) > len(right):
        return 1
    if len(left) < len(right):
        return -1

    for i in range(len(left)):
        if left[i] > right[i]:
            return 1
        if left[i] < right[i]:
            return -1

    return 0

c = divide_lists(a, b)
print(c)  # Output: ([1, 0, 2], [1, 0])

assert divide_lists([1, 2, 3, 4], [1, 2]) == ([1, 0, 2], [1, 0])
assert divide_lists([1, 2, 3], [4]) == ([3, 0], [3])
assert divide_lists([8, 4], [7]) == ([1, 2], [0])
assert divide_lists([1, 0, 0], [9]) == ([1, 1], [1])
assert divide_lists([5], [8]) == ([0], [5])
assert divide_lists([0], [3]) == ([0], [0])
assert divide_lists([1, 0, 0, 0], [2, 5]) == ([4, 0], [0])

print("All tests passed!")
