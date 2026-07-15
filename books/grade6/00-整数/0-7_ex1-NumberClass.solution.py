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
        return self.compare(other) < 0

    def __add__(self, other):
        """支持 self + other。"""
        return self.add(other)

    def __sub__(self, other):
        """支持 self - other。"""
        return self.subtract(other)

    def __mul__(self, other):
        """支持 self * other。"""
        return self.multiply(other)

    def __floordiv__(self, other):
        """支持 self // other，返回商。"""
        q, r = self.divide(other)  # q 是 quotient 的缩写，r 是 remainder 的缩写。
        return q

    def __mod__(self, other):
        """支持 self % other，返回余数。"""
        q, r = self.divide(other)  # q 是 quotient 的缩写，r 是 remainder 的缩写。
        return r

    def __divmod__(self, other):
        """支持 divmod(self, other)，返回商和余数。"""
        return self.divide(other)

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

        for i in range(len(left)):
            if left[i] > right[i]:
                return 1
            if left[i] < right[i]:
                return -1

        return 0

    def add(self, other):
        """把两个列表整数相加，返回新的 ListNumber。"""
        result = []
        carry = 0
        i = len(self.digits) - 1
        j = len(other.digits) - 1

        while i >= 0 or j >= 0 or carry > 0:
            digit_sum = carry
            if i >= 0:
                digit_sum += self.digits[i]
                i -= 1
            if j >= 0:
                digit_sum += other.digits[j]
                j -= 1

            result.insert(0, digit_sum % 10)
            carry = digit_sum // 10

        return ListNumber(result)

    def subtract(self, other):
        """计算 self - other，返回新的 ListNumber。"""
        if self.compare(other) < 0:
            raise ValueError("本题只处理大数减小数")

        result = []
        borrow = 0
        i = len(self.digits) - 1
        j = len(other.digits) - 1

        while i >= 0:
            top_d = self.digits[i] - borrow
            bottom_d = other.digits[j] if j >= 0 else 0

            if top_d < bottom_d:
                top_d += 10
                borrow = 1
            else:
                borrow = 0

            result.insert(0, top_d - bottom_d)
            i -= 1
            j -= 1

        return ListNumber(result)

    def multiply_by_one_digit(self, one_digit):
        """计算 self 乘以一位数。"""
        result = []
        carry = 0

        for i in range(len(self.digits) - 1, -1, -1):
            digit_product = self.digits[i] * one_digit + carry
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

        for i in range(len(other.digits) - 1, -1, -1):
            one_digit = other.digits[i]
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

        q_digits = []
        r = ListNumber([0])  # r 是 remainder 的缩写，表示当前余数。

        for d in self.digits:  # d 是 digit 的缩写，表示当前落下来的一位数字。
            r = ListNumber(r.digits + [d])

            q_d = 0  # q_d 是 quotient digit 的缩写，表示当前这一位的商。
            while r.compare(other) >= 0:
                r = r.subtract(other)
                q_d += 1

            q_digits.append(q_d)

        return ListNumber(q_digits), r


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
