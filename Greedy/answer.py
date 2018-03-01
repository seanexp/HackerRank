def greedy_florist(n, k, cost):
    min_cost = 0
    cost.sort()

    cnt = 0
    for i in range(n):
        quot = cnt // k
        min_cost += (quot + 1) * cost.pop()
        cnt += 1

    return min_cost


n, k = list(map(int, input().strip().split()))
cost = list(map(int, input().strip().split()))

print(greedy_florist(n, k, cost))
