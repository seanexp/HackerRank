from collections import deque


def game():
    """return least number of moves in which player can reach the target square
        if there is no solution, return -1"""
    global ladders
    global snake

    roll = [0 for _ in range(100+1)]
    visited = [False for _ in range(100+1)]
    visited[1] = True
    Q = deque()
    Q.append(1)

    while Q:
        u = Q.popleft()
        if roll[100]: break
        for i in range(1, 7):
            if u+i <= 100  and not visited[u+i]:
                l = ladders[u+i]
                s = snake[u+i]
                node = 0
                if l: node = l
                elif s: node = s
                else: node = u+i
                if not visited[node]:
                    Q.append(node)
                    roll[node] = roll[u] + 1
                    visited[node] = True


    return roll[100] if roll[100] else -1

with open('Snakes and Ladders.txt', 'rt') as f:
    T = int(f.readline().strip())

    for _ in range(T):
        N = int(f.readline().strip()) # number of ladders

        ladders = [0 for _ in range(100+1)]
        snake = [0 for _ in range(100+1)]
        for _ in range(N):
            start, end = list(map(int, f.readline().strip().split()))
            ladders[start] = end
        M = int(f.readline().strip()) # number of snakes
        for _ in range(M):
            start, end = list(map(int, f.readline().strip().split()))
            snake[start] = end

        print(game())
