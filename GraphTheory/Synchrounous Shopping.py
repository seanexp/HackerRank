with open('shopping.txt', 'rt') as f:
    N, M, K = list(map(int, f.readline().strip().split()))

    for _ in range(N):
        types = list(map(int, f.readline().strip().split()))[1:]

    for _ in range(M):
        a, b, w = list(map(int, f.readline().strip().split()))
