"""
扩充本章的有理数类，加入一些功能：
a)其他运算符的定义
b)各种比较和判断运算符的定义
c)转换到整数和浮点数的方法
d)给初始化函数加入从浮点数构造有理数的功能(Python标准库浮点数类型的as_integer_ratio()函数可以用在这里)

"""
class Rational(object):
    @staticmethod
    def __gcd(m, n):
        # 辗转求余法求最大公约数
        if n == 0:
            m, n = n, m
        while m != 0:
            m, n = n % m, m
        return n

    def __init__(self, num, den=1):
        # 构建有理数，分母默认传1，保证当分子传入整数时能够成功构建
        if not isinstance(num, int) or not isinstance(den, int):
            raise TypeError
        if den == 0:
            raise ZeroDivisionError
        sign = 1
        if den < 0:
            den, sign = -den, -sign
        if num < 0:
            num, sign = -num, -sign
        g = Rational.__gcd(num, den)
        self._num = sign*(num // g)
        self._den = den // g

    def __str__(self):
        return "%d/%d" % (self._num,self._den)

    @staticmethod
    def __check_type(num):
        # 自定义异常函数检查类型
        if not isinstance(num, Rational):
            raise TypeError(num)

    def add(self, another):
        # 加法
        Rational.__check_type(another)
        num = self._num * another._den + self._den*another._num
        den = self._den * another._den
        return Rational(num, den)

    def multiply(self,another):
        # 乘法
        Rational.__check_type(another)
        return Rational(self._num*another._num, self._den*another._den)

    def floor_divide(self, another):
        # 除法，结果为分数格式
        Rational.__check_type(another)
        return Rational(self._num*another._den,self._den*another._num)

    def minus(self, another):
        # 减法
        Rational.__check_type(another)
        num = self._num * another._den - self._den * another._num
        den = self._den * another._den
        return Rational(num, den)

    def true_divide(self, another):
        # 除法，结果为小数格式
        Rational.__check_type(another)
        num = self._num * another._den
        den = self._den * another._num
        return '%.2f' % (num/den)

    def equal(self, another):
        Rational.__check_type(another)
        return self._num*another._den == self._den*another._num

    def lessthan(self, another):
        Rational.__check_type(another)
        return self._num * another._den < self._den * another._num

    def lessequal(self, another):
        Rational.__check_type(another)
        return self._num*another._den <= self._den*another._num

    def greater(self, another):
        Rational.__check_type(another)
        return self._num * another._den > self._den * another._num

    def greaterequal(self, another):
        Rational.__check_type(another)
        return self._num * another._den >= self._den * another._num

if __name__ == '__main__':
    n = Rational(25,-30)
    m = Rational(10,15)
    print(n)
    print(m)
    print(n.add(m))
    print(n.multiply(m))
    print(n.floor_divide(m))
    print(n.lessthan(m))