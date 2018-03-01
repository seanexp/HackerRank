from copy import deepcopy


def count_luck(forest, K):
    """
    find path from 'M' to '*' and
    compare number of forked roads and K
    """

    trace = []

    def find_loc(forest, char):
        """find location of char in the forest"""
        num_of_rows = len(forest)
        num_of_cols = len(forest[0])

        for i in range(num_of_rows):
            for j in range(num_of_cols):
                if forest[i][j] == char:
                    return (i, j)

        raise ValueError

    def dfs(forest, point):
        nonlocal trace

        r, c = point
        if forest[r][c] == '*':
            trace.append(point)
            return
        forest[r][c] = 'X'

        for pt in [(r-1, c), (r, c+1), (r+1, c), (r, c-1)]:
            n, m = pt
            if forest[n][m] != 'X' and not trace:
                dfs(forest, pt)

        if trace:
            trace.append(point)

    start = find_loc(forest, 'M')

    dfs(deepcopy(forest), start)
    # gotta backtrace and find number of forked road
    cnt = 0  # number of forked road
    for i, pt in enumerate(trace[1:]):
        r, c = pt
        nbd = [(r-1, c), (r, c+1), (r+1, c), (r, c-1)]
        nbd.remove(trace[i])
        if i != len(trace) - 2:
            nbd.remove(trace[i+2])

        if list(map(lambda x: forest[x[0]][x[1]], nbd)).count('.'):
            cnt += 1

    return 'Impressed' if K == cnt else 'Oops!'


with open('luck.in', 'rt') as f:
    T = int(f.readline().strip())

    for _ in range(T):
        N, M = list(map(int, f.readline().strip().split()))

        forest = [list('X'*(M+2))]
        for _ in range(N):
            row = f.readline().strip()
            forest.append(list('X' + row + 'X'))
        forest.append(list('X'*(M+2)))

        K = int(f.readline().strip())

        print(count_luck(forest, K))
