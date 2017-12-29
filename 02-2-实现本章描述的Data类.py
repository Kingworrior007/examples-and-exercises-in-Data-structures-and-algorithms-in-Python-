"""
ADT Date:                                   #定义日期对象的抽象数据类型
    Date(int year,int month,int day)        #构造表示year/month/day的对象
    difference(Date d1,Date d2)             #求出d1和d2的日期差
    plus(Date d, int n)                     #计算出日期d之后n天的日期
    num_date(int year, int n)               #计算year年第n天的日期
    Adjust(Date d, int n)                   #将日期d调整n天
"""


class Date(object):
    def __init__(self, year, month, day):
        if not isinstance(year, int):
            raise TypeError(year)
        elif year < 0 or year > 9999:
            raise ValueError(year)
        else:
            self._year = year

        if not isinstance(month, int):
            raise TypeError(month)
        elif month < 1 or month > 12:
            raise ValueError(month)
        else:
            self._month = month

        if not isinstance(day, int):
            raise TypeError(day)
        elif day < 1:
            raise ValueError(day)
        else:
            self._day = day

    def __str__(self):
        return "%04d-%02d-%02d" % (self._year, self._month, self._day)

    @staticmethod
    def __leap_year(year):
        # 判断闰年
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            return True
        else:
            return False

    @staticmethod
    def __month_day_num(year, month):
        # 返回year年month月对应的天数，该方法需要简化
        days = {}
        leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        normal_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for i in range(12):
            if Date.__leap_year(year):
                days[i+1] = leap_year[i]
            else:
                days[i+1] = normal_year[i]
        return days[month]

    def __date_to_days(self):
        # 把实例对象的年月日转换为相对于00-01-01的天数，以方便比较
        total_days = 0
        for year in range(self._year):
            if Date.__leap_year(year):
                total_days += 366
            else:
                total_days += 365
        for month in range(1, self._month):
            total_days += Date.__month_day_num(self._year, month)
        total_days += self._day
        return total_days

    def difference(self, another):
        if not isinstance(another, Date):
            raise TypeError(another)
        dif_days = self.__date_to_days() - another.__date_to_days()
        return abs(dif_days)

    def plus(self, n):
        if not isinstance(n, int):
            raise TypeError(n)
        elif n < 0:
            raise ValueError(n)
        self._day += n
        while self._day > Date.__month_day_num(self._year, self._month):
            self._day -= Date.__month_day_num(self._year, self._month)
            self._month += 1
            if self._month == 13:
                self._month = 1
                self._year += 1
        return "%04d-%02d-%02d" % (self._year, self._month, self._day)

    @staticmethod
    def num_date(year, n):
        if not isinstance(n, int) or not isinstance(year, int):
            raise TypeError
        if n < 0:
            raise ValueError
        num_month =1
        num_year = year
        while n > Date.__month_day_num(num_year, num_month):
            n -= Date.__month_day_num(num_year, num_month)
            num_month += 1
            if num_month == 13:
                num_month = 1
                num_year += 1
        return "%04d-%02d-%02d" % (num_year, num_month, n)

    def adjust(self, n):
        if not isinstance(n, int):
            raise TypeError(n)
        if n >= 0:
            self.plus(n)
        else:
            self._day += n
            while self._day <= 0:
                self._day += Date.__month_day_num(self._year, self._month-1)
                self._month -= 1
                if self._month == 0:
                    self._month = 12
                    self._year -= 1
            return "%04d-%02d-%02d" % (self._year, self._month, self._day)

    def day(self):
        return self._day

    def month(self):
        return self._month

    def year(self):
        return self._year

if __name__ == '__main__':
    d = Date(2003, 12, 10)
    d1 = Date(2005, 2, 28)
    print(d)
    print("===")
    print(d.difference(d1))
    d.plus(30)
    print("===")
    print(d)
    print("===")
    d3 = Date(2006, 12, 13)
    d4 = d3.num_date(2016, 10)
    print(d4)
    d5 = d3.adjust(-20)
    print("===")
    print(d5)


