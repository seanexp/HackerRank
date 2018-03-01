def get_region(matrix):
    max_region = 0
    region = 0

    r = len(matrix)
    c = len(matrix[0])

    visited = [[False for _ in range(c)] for _ in range(r)]

    def isfilled(i, j):
        return True if matrix[i][j] == 1 else False

    def dfs(matrix, i, j):
        nonlocal visited
        nonlocal max_region
        nonlocal region
        region += 1
        visited[i][j] = True

        adj = [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1),
               (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]
        for u, v in adj:
            if isfilled(u, v) and not visited[u][v]:
                dfs(matrix, u, v)

    for i in range(1, r-1):
        for j in range(1, c-1):
            if isfilled(i, j) and not visited[i][j]:
                region = 0
                dfs(matrix, i, j)
                max_region = max(region, max_region)

    return max_region


with open('cells.in', 'rt') as f:
    n = int(f.readline().strip())
    m = int(f.readline().strip())

    matrix = [[0 for _ in range(m+2)]]

    for _ in range(n):
        row = list(map(int, f.readline().strip().split()))
        row.append(0)
        row.insert(0, 0)
        matrix.append(row)

    matrix.append([0 for _ in range(m+2)])

    print(get_region(matrix))
