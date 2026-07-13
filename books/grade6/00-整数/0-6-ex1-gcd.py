"""题目：求两个数的最大公约数。

公约数就是“能同时整除两个数的数”。
最大公约数就是所有公约数中最大的一个。
例如 12 和 18 的公约数有 1、2、3、6，所以最大公约数是 6。

要求：
1. 编写 gcd(a, b)。
2. 从 1 开始检查每个可能的因数。
3. 如果一个数能同时整除 a 和 b，就记录下来。
4. 返回最大的那个公约数。

例子：
gcd(12, 18) 返回 6。
"""

number1 = 12
number2 = 18

def gcd(a, b):
    """求两个正整数的最大公约数。

    Args:
        a (int): 第一个正整数。
        b (int): 第二个正整数。

    Returns:
        int: a 和 b 的最大公约数。
    """
    # Todo Begin
    pass
    # Todo End

answer = gcd(number1, number2)
print(answer)  # Output: 6

assert gcd(12, 18) == 6
assert gcd(8, 20) == 4
assert gcd(7, 13) == 1
assert gcd(15, 30) == 15
assert gcd(21, 28) == 7
