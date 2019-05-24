import random

def merge(l1, l2):
    for i in range(len(l1)):
        n = l1[i]
        l2.append(n)
    return sorted(l2)


def delete(alist):
    dict = {}
    l = []
    for i in range(len(alist)):
        n = alist[i]
        dict[n] = 1
    for k in dict.keys():
        l.append(k)
    return l


def randomColor():
    tup = ()
    i = 0
    while i < 3:
        n = random.randint(0, 256)
        tup1 = (n,)
        tup += tup1
        i += 1
    return tup


def sort(alist):
    for i in range(len(alist)):
        for j in range(len(alist) - 1):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
    return alist


if __name__ == '__main__':
    l1 = [1, 3, 5]
    l2 = [2, 4, 6, 7]
    l3 = [1, 1, 1, 2, 2, 3, 3, 5, 4, 4]
    l4 = [4, 6, 2, 8, 1, 3]
    print(merge(l1, l2))
    print(delete(l3))
    print(randomColor())
    print(sorted(l4))
