"""题目：判断一个数是不是质数。

一个数如果只能被 1 和自己整除，它就是质数。
例如 7 是质数，9 不是质数，因为 9 可以被 3 整除。

要求：
1. 编写 is_prime(x)。
2. 是质数就返回 True，不是质数就返回 False。
3. 注意：1 不是质数。
"""

number = 7

def is_prime(x):
    """判断一个整数是不是质数。

    Args:
        x (int): 要判断的整数。

    Returns:
        bool: 如果 x 是质数，返回 True；否则返回 False。
    """
    # Todo Begin
    if x < 2:
        return False

    for factor in range(2, x):
        if x % factor == 0:
            return False

    return True
    # Todo End

answer = is_prime(number)
print(answer)  # Output: True

assert is_prime(1) == False
assert is_prime(2) == True
assert is_prime(7) == True
assert is_prime(9) == False
assert is_prime(10) == False
