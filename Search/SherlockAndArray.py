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


with open('sherlock.in', 'rt') as f:
    T = int(f.readline().strip())

    for _ in range(T):
        n = int(f.readline().strip())
        A = list(map(int, f.readline().strip().split()))

        print(sherlock(n, A))
