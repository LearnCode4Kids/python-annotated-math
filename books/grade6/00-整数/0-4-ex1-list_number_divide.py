"""题目：用列表表示的数字做除法。

已知两个列表。每个元素都是 0 到 9 的整数，按从左到右的顺序表示一个数。
例如 [1, 2, 3] 表示 123，[4] 表示 4。

要求：
1. 编写 divide_lists(list1, list2)。
2. list2 表示的数不能是 0。
3. 像人做竖式除法一样，从左到右一位一位处理 list1。
4. 返回两个新列表：商列表和余数列表。
5. 不要修改原来的两个列表。

例子：
[1, 2, 3] 除以 [4]，返回 ([3, 0], [3])。
因为 123 ÷ 4 = 30 余 3。
"""

a = [1, 2, 3]  # as a number
b = [4]  # as a number

def divide_lists(list1, list2):
    """把两个列表表示的整数相除，返回商列表和余数列表。

    Args:
        list1 (list[int]): 被除数列表，表示一个整数。
        list2 (list[int]): 除数列表，表示一个非零整数。

    Returns:
        tuple[list[int], list[int]]: 商列表和余数列表。
    """
    # Todo Begin
    # Hint: 先比较 list1 和 list2 的大小，如果 list1 < list2，商为 0，余数为 list1。
    # 如果 list1 >= list
    # 变量英文全称，变量缩写，中文含义
    # quotient q 商
    # remainder r 余数
    q = [0]
    r = list1[:]
    
    # Todo End  
    
    
    return q, r



def add_lists(list1, list2):
    """把两个列表表示的数相加，返回一个新的列表。

    Args:
        list1 (list[int]): 第一个列表，表示一个数。
        list2 (list[int]): 第二个列表，表示一个数。

    Returns:
        list[int]: 考虑进位后的结果列表。
    """
    
    # Todo Begin
    # Hint: 将列表变得一样长，短的前面补 0，然后按位相加，考虑进位。
    while len(list1) < len(list2):
        list1.insert(0, 0)
    while len(list2) < len(list1):
        list2.insert(0, 0)
    # Todo End
    
    result = []
    carry = 0

    for index in range(len(list1) - 1, -1, -1):
        digit_sum = list1[index] + list2[index] + carry
        result.insert(0, digit_sum % 10)
        carry = digit_sum // 10

    if carry > 0:
        result.insert(0, carry)
    
    return result


def subtract_lists(list1, list2):
    """把两个列表表示的整数相减，返回一个新的列表。

    Args:
        list1 (list[int]): 被减数列表，表示一个整数。
        list2 (list[int]): 减数列表，表示一个整数。

    Returns:
        list[int]: list1 - list2 的结果列表。
    """
    result = []
    carrier = 0
    index1 = len(list1) - 1
    index2 = len(list2) - 1

    while index1 >= 0:
        top_digit = list1[index1] - carrier
        bottom_digit = list2[index2] if index2 >= 0 else 0

        if top_digit < bottom_digit:
            top_digit += 10
            carrier = 1
        else:
            carrier = 0

        result.insert(0, top_digit - bottom_digit)
        index1 -= 1
        index2 -= 1

    while len(result) > 1 and result[0] == 0:
        result.pop(0)

    return result




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

c = divide_lists(a, b)
print(c)  # Output: ([3, 0], [3])

assert divide_lists([1, 2, 3], [4]) == ([3, 0], [3])
assert divide_lists([8, 4], [7]) == ([1, 2], [0])
assert divide_lists([1, 0, 0], [9]) == ([1, 1], [1])
assert divide_lists([5], [8]) == ([0], [5])
assert divide_lists([0], [3]) == ([0], [0])

print("All tests passed!")