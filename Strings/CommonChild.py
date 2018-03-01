#  Did not pass all the cases in python3 but pypy3 worked
def commonchild(a, b):
    arr = [[0 for _ in range(len(a))] for _ in range(len(b))]

    # initialization
    arr[0][0] = 1 if a[0] == b[0] else 0

    for i in range(1, len(b)):
        if arr[0][i-1]:
            arr[0][i] = arr[0][i-1]
        elif a[0] == b[i]:
            arr[0][i] = 1
        else:
            arr[0][i] = 0

    for i in range(1, len(a)):
        if arr[i-1][0]:
            arr[i][0] = arr[i-1][0]
        elif b[0] == a[i]:
            arr[i][0] = 1
        else:
            arr[i][0] = 0

    for i in range(1, len(a)):
        for j in range(1, len(b)):
            if a[i] == b[j]:
                arr[i][j] = arr[i-1][j-1] + 1
            else:
                arr[i][j] = max(arr[i-1][j], arr[i][j-1])

    return arr[-1][-1]


with open('common.in', 'rt') as f:
    a = f.readline().strip()
    b = f.readline().strip()

    print(commonchild(a, b))
