def parlor(m, n, cost):
    sorted_cost = sorted(cost)
    pos = dict()

    for i in range(n):
        li = pos.get(cost[i], [])
        li.append(i+1)
        pos[cost[i]] = li

    i = 0
    j = n - 1
    while i < n and i < j:
        if sorted_cost[i] + sorted_cost[j] < m:
            i += 1
        elif sorted_cost[i] + sorted_cost[j] > m:
            j -= 1
        else:
            break

    idx1 = pos[sorted_cost[i]].pop()
    idx2 = pos[sorted_cost[j]].pop()

    return '{} {}'.format(min(idx1, idx2), max(idx1, idx2))


with open('icecream.in', 'rt') as f:
    t = int(f.readline().strip())

    for _ in range(t):
        m = int(f.readline().strip())  # money
        n = int(f.readline().strip())
        cost = list(map(int, f.readline().strip().split()))

        print(parlor(m, n, cost))
