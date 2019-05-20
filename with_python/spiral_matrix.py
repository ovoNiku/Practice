"""
1  2  3  4  5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
"""


def generation(a):
    return [[i] * a for i in range(a)]


def process(matrix, n, min_x=0, min_y=0, count=1):
    if n == 1:
        matrix[min_x][min_y] = count
        return
    x = min_x
    y = min_y
    max_x = n + min_x
    max_y = n + min_y
    mode = True
    while n > 1:
        matrix[y][x] = count
        if mode:
            if x < max_x - 1:
                x += 1
            else:
                y += 1
            if y == max_y - 1:
                mode = False
        else:
            if x > min_x:
                x -= 1
            else:
                y -= 1
            if y <= min_y:
                # 跑完一圈啦
                n -= 2
                process(matrix, n, min_x + 1, min_y + 1, count + 1)
                break
        count += 1


def output(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(str(matrix[i][j]) + "\t", end="")
        print("\n")


if __name__ == '__main__':
    size = 5
    m = generation(size)
    process(m, size)
    output(m)
