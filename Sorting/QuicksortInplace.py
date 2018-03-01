def partition(ar, p, r):
    pivot = ar[r]
    i = p - 1
    j = p
    while j < r:
        if ar[j] < pivot:
            ar[i+1], ar[j] = ar[j], ar[i+1]
            i += 1
        j += 1
    ar[i+1], ar[r] = ar[r], ar[i+1]

    return i+1


def quicksort(ar, p, r):
    if p >= r:
        return
    i = partition(ar, p, r)
    print(*ar, sep=' ')
    quicksort(ar, p, i-1)
    quicksort(ar, i+1, r)


n = int(input().strip())
ar = list(map(int, input().strip().split()))
quicksort(ar, 0, n - 1)
