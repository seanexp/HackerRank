def even_tree(N):
    cnt = 0
    visited = [False for _ in range(N+1)]
    def traverse(node):
        global children
        nonlocal cnt
        nonlocal visited
        visited[node] = True
        if not children[node]:
            return 1

        num_of_family = 0
        for child in children[node]:
            if not visited[child]:
                descendents = traverse(child)
                if descendents % 2 == 0:
                    cnt += 1

                num_of_family += descendents

        return num_of_family + 1

    traverse(1)
    return cnt

with open('Even Tree.txt', 'rt') as f:
    N, M = list(map(int, f.readline().strip().split()))

    children = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = list(map(int, f.readline().strip().split()))
        children[a].append(b)
        children[b].append(a)

    print(even_tree(N))
