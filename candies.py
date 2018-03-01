import logging


def is_locmin(ratings, idx):
    if idx == 0 and ratings[idx] <= ratings[idx+1]:
        return True
    if idx == len(ratings) - 1 and ratings[idx] <= ratings[idx-1]:
        return True
    if ratings[idx-1] >= ratings[idx] and ratings[idx] <= ratings[idx+1]:
        return True

    return False


def is_locmax(ratings, idx):
    if idx == 0 and ratings[idx] >= ratings[idx+1]:
        return True
    if idx == len(ratings) - 1 and ratings[idx] >= ratings[idx-1]:
        return True
    if ratings[idx-1] <= ratings[idx] and ratings[idx] > ratings[idx+1]:
        return True

    return False


def get_next_locmin(ratings, idx):
    for i in range(idx, len(ratings)):
        if is_locmin(ratings, i):
            return i

    return -1

def get_next_locmax(ratings, idx):
    for i in range(idx, len(ratings)):
        if is_locmax(ratings, i):
            return i

    return -1

def candies(ratings, n):
    min_candies = 0
    curr = 0
    next_min = 0
    for i in range(n):
        if is_locmin(ratings, i):
            curr = 1
        elif is_locmax(ratings, i):
            next_min = get_next_locmin(ratings, i)
            if i > 0 and ratings[i] == ratings[i-1]:
                curr = next_min - i + 1
            else:
                curr = max(curr+1, next_min - i + 1)
        elif ratings[i-1] < ratings[i]:
            curr += 1
        elif ratings[i-1] > ratings[i]:
            curr = next_min - i + 1
        else:
            logging.wargning("corner case!")

        min_candies += curr

        print((ratings[i], curr))

    return min_candies

# N = int(input().strip())
# ratings = []

# for _ in range(N):
#     temp = int(input().strip())
#     ratings.append(temp)
#
# print(candies(ratings, N))


with open('./test.txt', 'r') as f:
    N = int(f.readline().strip())
    ratings = []

    for _ in range(N):
        temp = int(f.readline().strip())
        ratings.append(temp)

    print(candies(ratings, N))

