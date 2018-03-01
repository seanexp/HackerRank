#!/bin/python3

import sys


visited = [False for i in range(10**5 + 1)]
outward_roads = [[] for i in range(10**5 + 1)]

def dfs(city): # -> number of cities in a component
    if visited[city]: return 0
    else:
        visited[city] = True
        unvisited_adj = list(filter(lambda x: not visited[x], outward_roads[city]))

        cnt = 1
        for adj in unvisited_adj:
            cnt += dfs(adj)

        return cnt

q = int(input().strip())
for a0 in range(q):
    n,m,x,y = input().strip().split(' ')
    # n: number of cities, m: number of roads
    n,m,c_lib,c_road = [int(n),int(m),int(x),int(y)]
    for a1 in range(m):
        city_1,city_2 = input().strip().split(' ')
        city_1,city_2 = [int(city_1),int(city_2)]
        outward_roads[city_1].append(city_2)
        outward_roads[city_2].append(city_1)

    if c_lib <= c_road: print(c_lib * n)
    else:
        components = []
        for city in range(1, n+1):
            if not visited[city]:
                components.append(dfs(city))

        libs = len(components)
        roads = n - libs

        print(libs * c_lib + roads * c_road)

    visited = [False for i in range(10**5 + 1)]
    outward_roads = [[] for i in range(10**5 + 1)]
