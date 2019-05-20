"""
1 5 8 9 15 19 20 25
输入14返回false
输入15返回true
"""


def search(alist, n):
    l = len(alist)
    mid = l // 2
    if l == 1:
        if alist[0] != n:
            return False
        else:
            return True
    if alist[mid] > n:
        return search(alist[:mid], n)
    elif alist[mid] < n:
        if l > mid + 1:
            return search(alist[mid + 1:], n)
        else:
            return False


def search_other(alist, n):
    l = len(alist)
    first = 0
    last = l - 1
    while first <= last:
        mid = (first + last) // 2
        if alist[mid] > n:
            last = mid - 1
        elif alist[mid] < n:
            first = mid + 1
        else:
            return True
    return False


def test_search():
    list = [1, 5, 8, 9, 15, 19, 20, 25]
    assert (search(list, 6) is False)
    assert (search(list, 9) is True)
    assert (search(list, -1) is False)
    assert (search_other(list, 6) is False)
    assert (search_other(list, 9) is True)
    assert (search_other(list, -1) is False)


if __name__ == '__main__':
    test_search()
