def separate(s):
    k = 1
    while k <= len(s) // 2:
        init = num = s[:k]
        tests = s
        while tests.startswith(num):
            tests = tests[len(num):]
            new_num = int(num) + 1
            num = str(new_num)

        if not tests:
            return "YES " + init

        k += 1

    return "NO"


with open('./numbers.in', 'rt') as f:
    q = int(f.readline().strip())

    for _ in range(q):
        s = f.readline().strip()
        print(separate(s))
