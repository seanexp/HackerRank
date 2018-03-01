def lcs(n, m, A, B):
    arr = [[[] for _ in range(m)] for _ in range(n)]

    # initialization
    arr[0][0] = [A[0]] if A[0] == B[0] else []

    for i in range(1, m):
        if arr[0][i-1]:
            arr[0][i] = arr[0][i-1]
        elif A[0] == B[i]:
            arr[0][i] = [A[0]]

    for i in range(1, n):
        if arr[i-1][0]:
            arr[i][0] = arr[i-1][0]
        elif B[0] == A[i]:
            arr[i][0] = [B[0]]

    for i in range(1, n):
        for j in range(1, m):
            if A[i] == B[j]:
                arr[i][j] = arr[i-1][j-1] + [A[i]]
            else:
                arr[i][j] = max(arr[i-1][j], arr[i][j-1], key=len)

    return " ".join([str(x) for x in arr[-1][-1]])


with open('longest.in', 'rt') as f:
    n, m = list(map(int, f.readline().strip().split()))
    A = list(map(int, f.readline().strip().split()))
    B = list(map(int, f.readline().strip().split()))

    print(lcs(n, m, A, B))
