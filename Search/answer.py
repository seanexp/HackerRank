def sherlock(n, A):
    left_sum = 0
    right_sum = sum(A)

    for a in A:
        right_sum -= a
        if left_sum == right_sum:
            return 'YES'
        else:
            left_sum += a

    return 'NO'


T = int(input().strip())

for _ in range(T):
    n = int(input().strip())
    A = list(map(int, input().strip().split()))

    print(sherlock(n, A))
