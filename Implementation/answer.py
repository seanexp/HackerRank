def knums(p, q):
    kaprekar_nums = []

    for i in range(p, q+1):
        squarestr = str(i**2)
        k = len(squarestr) - len(str(i))
        l = int(squarestr[:k]) if squarestr[:k] else 0
        r = int(squarestr[k:])
        if i == l+r:
            kaprekar_nums.append(i)

    return " ".join([str(x) for x in kaprekar_nums]) if kaprekar_nums else "INVALID RANGE"

p = int(input().strip())
q = int(input().strip())
print(knums(p, q))
