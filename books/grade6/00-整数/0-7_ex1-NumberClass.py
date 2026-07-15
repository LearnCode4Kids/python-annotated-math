"""题目：用列表实现一个整数类。

前面我们已经用列表做过整数的比较、加法、减法、乘法和除法。
现在把这些能力放到一个类里，让每个数字自己“会计算”。

例如：
ListNumber([1, 2, 3]) 表示 123。
ListNumber([4, 5]) 表示 45。

要求：
1. 编写 ListNumber 类。
2. 用 self.digits 保存数字列表。
3. 实现 compare、add、subtract、multiply、divide。
4. divide 返回两个 ListNumber：商和余数。
5. 在当前实现上，补充操作符重载。
6. 支持 a + b、a - b、a * b、a // b、a % b、divmod(a, b)。
7. 不要修改参加计算的原数字。
"""


class ListNumber:
    """用列表保存一个非负整数。"""

    def __init__(self, digits):
        self.digits = self.remove_leading_zeros(digits[:])

    def __repr__(self):
        return f"ListNumber({self.digits})"

    def __eq__(self, other):
        return isinstance(other, ListNumber) and self.digits == other.digits

    def __lt__(self, other):
        """支持 self < other。"""
        # Todo Begin
        pass
        # Todo End

    def __add__(self, other):
        """支持 self + other。"""
        # Todo Begin
        pass
        # Todo End

    def __sub__(self, other):
        """支持 self - other。"""
        # Todo Begin
        pass
        # Todo End

    def __mul__(self, other):
        """支持 self * other。"""
        # Todo Begin
        pass
        # Todo End

    def __floordiv__(self, other):
        """支持 self // other，返回商。"""
        # Todo Begin
        pass
        # Todo End

    def __mod__(self, other):
        """支持 self % other，返回余数。"""
        # Todo Begin
        pass
        # Todo End

    def __divmod__(self, other):
        """支持 divmod(self, other)，返回商和余数。"""
        # Todo Begin
        pass
        # Todo End

    @staticmethod
    def remove_leading_zeros(digits):
        """去掉开头多余的 0，但保留数字 0 自己。"""
        while len(digits) > 1 and digits[0] == 0:
            digits.pop(0)
        return digits

    def compare(self, other):
        """比较两个 ListNumber 的大小。

        Returns:
            int: self 更大返回 1，相等返回 0，更小返回 -1。
        """
        left = self.digits[:]
        right = other.digits[:]

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

    def add(self, other):
        """把两个列表整数相加，返回新的 ListNumber。"""
        result = []
        carry = 0
        index1 = len(self.digits) - 1
        index2 = len(other.digits) - 1

        while index1 >= 0 or index2 >= 0 or carry > 0:
            digit_sum = carry
            if index1 >= 0:
                digit_sum += self.digits[index1]
                index1 -= 1
            if index2 >= 0:
                digit_sum += other.digits[index2]
                index2 -= 1

            result.insert(0, digit_sum % 10)
            carry = digit_sum // 10

        return ListNumber(result)

    def subtract(self, other):
        """计算 self - other，返回新的 ListNumber。"""
        if self.compare(other) < 0:
            raise ValueError("本题只处理大数减小数")

        result = []
        carrier = 0
        index1 = len(self.digits) - 1
        index2 = len(other.digits) - 1

        while index1 >= 0:
            top_digit = self.digits[index1] - carrier
            bottom_digit = other.digits[index2] if index2 >= 0 else 0

            if top_digit < bottom_digit:
                top_digit += 10
                carrier = 1
            else:
                carrier = 0

            result.insert(0, top_digit - bottom_digit)
            index1 -= 1
            index2 -= 1

        return ListNumber(result)

    def multiply_by_one_digit(self, one_digit):
        """计算 self 乘以一位数。"""
        result = []
        carry = 0

        for index in range(len(self.digits) - 1, -1, -1):
            digit_product = self.digits[index] * one_digit + carry
            result.insert(0, digit_product % 10)
            carry = digit_product // 10

        while carry > 0:
            result.insert(0, carry % 10)
            carry = carry // 10

        return ListNumber(result)

    def multiply(self, other):
        """用竖式乘法计算两个 ListNumber 的乘积。"""
        result = ListNumber([0])
        zeros_count = 0

        for index in range(len(other.digits) - 1, -1, -1):
            one_digit = other.digits[index]
            partial_result = self.multiply_by_one_digit(one_digit)

            if partial_result.digits != [0]:
                partial_result = ListNumber(partial_result.digits + [0] * zeros_count)

            result = result.add(partial_result)
            zeros_count += 1

        return result

    def divide(self, other):
        """用竖式除法计算 self 除以 other。

        Returns:
            tuple[ListNumber, ListNumber]: 商和余数。
        """
        if other.digits == [0]:
            raise ValueError("除数不能是 0")

        quotient_digits = []
        remainder = ListNumber([0])

        for digit in self.digits:
            remainder = ListNumber(remainder.digits + [digit])

            quotient_digit = 0
            while remainder.compare(other) >= 0:
                remainder = remainder.subtract(other)
                quotient_digit += 1

            quotient_digits.append(quotient_digit)

        return ListNumber(quotient_digits), remainder


a = ListNumber([1, 2, 3])
b = ListNumber([4, 5])

print(a.add(b))       # Output: ListNumber([1, 6, 8])
print(a.subtract(ListNumber([7, 8])))  # Output: ListNumber([4, 5])
print(a.multiply(b))  # Output: ListNumber([5, 5, 3, 5])
print(a.divide(ListNumber([4])))       # Output: (ListNumber([3, 0]), ListNumber([3]))
print(a + b)          # Output: ListNumber([1, 6, 8])
print(a // ListNumber([4]))  # Output: ListNumber([3, 0])
print(a % ListNumber([4]))   # Output: ListNumber([3])

assert ListNumber([0, 0, 5]).digits == [5]
assert ListNumber([3, 5, 6]).compare(ListNumber([4, 7])) == 1
assert ListNumber([5, 6]).add(ListNumber([4, 7, 8])) == ListNumber([5, 3, 4])
assert ListNumber([5, 0, 2]).subtract(ListNumber([7, 8])) == ListNumber([4, 2, 4])
assert ListNumber([1, 2, 3]).multiply(ListNumber([4, 5])) == ListNumber([5, 5, 3, 5])
assert ListNumber([1, 2, 3]).divide(ListNumber([4])) == (ListNumber([3, 0]), ListNumber([3]))
assert ListNumber([8, 4]).divide(ListNumber([7])) == (ListNumber([1, 2]), ListNumber([0]))
assert ListNumber([5]).divide(ListNumber([8])) == (ListNumber([0]), ListNumber([5]))
assert ListNumber([4, 7]) < ListNumber([3, 5, 6])
assert ListNumber([1, 2, 3]) + ListNumber([4, 5]) == ListNumber([1, 6, 8])
assert ListNumber([5, 0, 2]) - ListNumber([7, 8]) == ListNumber([4, 2, 4])
assert ListNumber([1, 2, 3]) * ListNumber([4, 5]) == ListNumber([5, 5, 3, 5])
assert ListNumber([1, 2, 3]) // ListNumber([4]) == ListNumber([3, 0])
assert ListNumber([1, 2, 3]) % ListNumber([4]) == ListNumber([3])
assert divmod(ListNumber([1, 2, 3]), ListNumber([4])) == (ListNumber([3, 0]), ListNumber([3]))

print("All tests passed!")
