"""
Shortest Path
"""
import numpy as np
def readgraph(file):
    f = open(file, 'r')
    f.readline()
    g = {i: {} for i in range(1, 1001)}
    ls = f.readline()
    while ls:
        data = list(map(int, ls.split(' ')))
        g[data[0]][data[1]] = data[2]
        ls = f.readline()
    f.close()
    return g


def askmin(g):
    n = 1000
    A = [[0 if i == j else g[i+1].get(j+1, np.inf) for j in range(n)] for i in range(n)]
    for k in range(n):
        if k % 100 == 0:
            print(k)
        for i in range(n):
            for j in range(n):
                A[i][j] = min(A[i][j], A[i][k] + A[k][j])
    for i in range(n):
        if A[i][i] < 0:
            print('error at %i' % (i+1))
    print('min=%i' % min(min(row) for row in A))


g1 = readgraph('g1.txt')
g2 = readgraph('g2.txt')
g3 = readgraph('g3.txt')

print('g1')
askmin(g1)
print('g2')
askmin(g2)
print('g3')
askmin(g3)
