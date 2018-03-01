def homework(n, arr):

    pos = dict()
    for i, num in enumerate(arr):
        pos[num] = i

    cnt = 0
    sorted_arr = sorted(arr)

    for i in range(len(arr)):
        if arr[i] != sorted_arr[i]:
            cnt += 1

            new_idx = pos[sorted_arr[i]]
            pos[arr[i]] = new_idx
            arr[i], arr[new_idx] = arr[new_idx], arr[i]

    return cnt


with open('homework.in', 'rt') as f:
    n = int(f.readline().strip())
    arr = list(map(int, f.readline().strip().split()))

    asc = homework(n, arr.copy())
    desc = homework(n, list(reversed(arr)))
    print(min(asc, desc))
