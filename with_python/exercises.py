# 判断是否为水仙花数
def foo(a):
    s = str(a)
    n = 0
    for i in s:
        i = int(i)
        n += (i ** len(s))
    return n == a


# 返回第n个斐波那契数
def fiber(n):
    if n == 1 or n == 2:
        rs = 1
        return rs
    else:
        count = 2
        n1 = 1
        n2 = 1
        rs = 0
        while count < n:
            rs = n1 + n2
            n1 = n2
            n2 = rs
            count += 1
        return rs


# n的阶乘
def factorial(n):
    i = 1
    rs = 1
    while i < n:
        rs *= (i + 1)
        i += 1
    return rs


# 从1到n的平方和
def add_squares(n):
    i = 1
    rs = 1
    while i < n:
        rs += (i + 1) ** 2
        i += 1
    return rs


# 判断是否为回文
def str_symmetry(s):
    s = str(s)
    l = len(s)
    if (l % 2) == 0:
        half = l // 2
        s1 = s[:half]
        s2 = s[half:][::-1]
        return s1 == s2
    else:
        return False


# 判断字符串中的括号是否匹配
def single_symmetry(s):
    stack = []
    for i in s:
        if i == '[' or i == '(':
            stack.append(i)
        if i == ']' or i == ')':
            a = ''
            a += stack.pop()
            a += i
            if a == '[]' or a == '()':
                r = True
            else:
                return False
    return r


def test_foo():
    assert (foo(153) is True)
    assert (foo(123) is False)
    assert (foo(1634) is True)
    assert (foo(1234) is False)
    assert (foo(54748) is True)
    assert (foo(16345) is False)
    assert (foo(4210818) is True)
    assert (foo(1634345) is False)


def test_fiber():
    assert (fiber(1) == 1)
    assert (fiber(2) == 1)
    assert (fiber(4) == 3)
    assert (fiber(5) == 5)


def test_factorial():
    assert (factorial(1) == 1)
    assert (factorial(4) == 24)


def test_add_squares():
    assert (add_squares(3) == 14)
    assert (add_squares(1) == 1)


def test_str_symmetry():
    assert (str_symmetry(123321) is True)
    assert (str_symmetry('abccba') is True)
    assert (str_symmetry(123) is False)
    assert (str_symmetry('abcd') is False)


def test_single_symmetry():
    assert (single_symmetry('[(])') is False)
    assert (single_symmetry('[()]') is True)
    assert (single_symmetry('1[2(3)4]5') is True)
    assert (single_symmetry('[())]') is False)


if __name__ == '__main__':
    test_foo()
    test_fiber()
    test_factorial()
    test_add_squares()
    test_str_symmetry()
    test_single_symmetry()
