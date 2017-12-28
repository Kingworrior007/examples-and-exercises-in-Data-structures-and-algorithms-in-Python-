"""
第2章 编程练习
1. 定义一个表示时间的类Time，它提供下面操作：
a) Time(hours, minutes, seconds)创建一个时间对象；
b) t.hours()、t.minutes()、t.seconds分别返回时间对象t的小时、分钟和秒值；
c) 为Time对象定义加法和减法操作（用运算符+和-）；
d) 定义时间对象的等于和小于关系运算（用运算符==和<）
"""


class TimeTypeError(TypeError):
    pass


class TimeValueError(ValueError):
    pass


class Time(object):
    def __init__(self, hours, minutes, seconds):
        if 0 <= hours <= 23:
            self._hours = hours
        else:
            raise TimeValueError('ValueError', hours)
        if 0 <= minutes <= 59:
            self._minutes = minutes
        else:
            raise TimeValueError('ValueError', minutes)
        if 0 <= minutes <= 59:
            self._seconds = seconds
        else:
            raise TimeValueError('ValueError', seconds)

        self._seconds_total = hours * 3600 + minutes * 60 + seconds

    def __str__(self):
        return "%02d:%02d:%02d" % (self._hours, self._minutes, self._seconds)

    def hours(self):
        return self._hours

    def minutes(self):
        return self._minutes

    def seconds(self):
        return self._minutes

    def time_add(self, another):
        if not isinstance(another, Time):
            raise TimeTypeError('TypeError', another)
        time_add_seconds = self._seconds_total + another._seconds_total
        hour = time_add_seconds // 3600
        minute = (time_add_seconds - hour * 3600) // 60
        second = time_add_seconds % 60
        hour %= 24
        return "%02d:%02d:%02d" % (hour, minute, second)

    def time_minus(self, another):
        if not isinstance(another, Time):
            raise TimeTypeError('TypeError', another)
        if not self.time_lt(another):
            time_minus_seconds = self._seconds_total - another._seconds_total
            hour = time_minus_seconds // 3600
            minute = (time_minus_seconds - hour * 3600) // 60
            second = time_minus_seconds % 60
            hour %= 24
            return "%02d:%02d:%02d" % (hour, minute, second)
        else:
            return 'can not minus larger time!'

    def time_equal(self, another):
        if not isinstance(another, Time):
            raise TimeTypeError('TypeError', another)
        return self._seconds_total == another._seconds_total

    def time_lt(self, another):
        if not isinstance(another, Time):
            raise TimeTypeError('TypeError', another)
        return self._seconds_total < another._seconds_total


if __name__ == "__main__":
    t1 = Time(20, 20, 5)
    print(t1)
    t2 = Time(12, 50, 5)
    t3 = [1, 2, 3]
    print(t2)

    print(t2.time_minus(t1))
    # print(t1.time_add(t3))
    print(t2.time_lt(t1))
    print(t1.time_equal(t1))









