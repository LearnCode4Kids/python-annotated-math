"""题目：把一个数分解成质因数。

质因数就是“能整除这个数的质数因数”。
例如 12 可以分成 2、2、3，因为 2 * 2 * 3 = 12。

要求：
1. 编写 num_to_factors(x)。
2. 返回一个列表，里面放 x 的质因数。
3. 从小到大放入列表。

例子：
num_to_factors(12) 返回 [2, 2, 3]。
"""

number = 12

def num_to_factors(x):
    """将一个整数分解为质因数。

    Args:
        x (int): 要分解的整数。

    Returns:
        list: 包含 x 的质因数的列表。
    """
    # Todo Begin
    factors = []
    divisor = 2

    while x > 1:
        if x % divisor == 0:
            factors.append(divisor)
            x = x // divisor
        else:
            divisor += 1

    return factors
    # Todo End

factors = num_to_factors(number)
print(factors)  # Output: [2, 2, 3]

assert num_to_factors(2) == [2]
assert num_to_factors(6) == [2, 3]
assert num_to_factors(12) == [2, 2, 3]
assert num_to_factors(18) == [2, 3, 3]
assert num_to_factors(25) == [5, 5]
