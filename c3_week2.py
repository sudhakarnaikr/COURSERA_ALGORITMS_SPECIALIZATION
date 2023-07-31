"""
k-clustering
"""

f = open('clustering1.txt', 'r')

graph = {}
f.readline()
ls = f.readline()
while ls:
    data = list(map(int, ls.split(' ')))
    graph[(data[0], data[1])] = data[2]
    ls = f.readline()
f.close()

g = graph.copy()

c = list(range(1, 501))
cnum = 500
while True:
    edge = min(g, key=g.get)
    d = g.pop(edge)
    l1, l2 = c[edge[0]-1], c[edge[1]-1]
    if l1 != l2 and cnum > 4:
        cnum -= 1
        for i in range(500):
            c[i] = l1 if c[i] == l2 else c[i]
    elif l1 != l2 and cnum == 4:
        print(edge, l1, l2, d)
        break

"""
k-clustering
"""

f = open('clustering_big.txt', 'r')

f.readline()
ls = f.readline()
graph = []
while ls:
    graph += [ls[:-1].replace(' ', '')]
    ls = f.readline()
f.close()

graph = list(set(graph))
N = len(graph)
gn = [int(i, 2) for i in graph]


def nb(v):
    n = 24
    data = []
    for i in range(n):
        s = list(v)
        s[i] = '1' if s[i] == '0' else '0'
        data += [int(''.join(s), 2)]
        for j in range(i+1, n):
            ss = s.copy()
            ss[j] = '1' if ss[j] == '0' else '0'
            data += [int(''.join(ss), 2)]
    return data


uf = {i: i for i in gn}
rank = {i: 0 for i in gn}


def find(i):
    global uf
    if uf[i] == i:
        return i
    elif uf[uf[i]] == uf[i]:
        return uf[i]
    else:
        newi = uf[i]
        while uf[newi] != newi:
            newi = uf[newi]
        uf[i] = newi
        return newi


def merge(i, j):
    global uf, rank
    i, j = find(i), find(j)
    if i != j:
        if rank[i] > rank[j]:
            uf[j] = i
        elif rank[i] < rank[j]:
            uf[i] = j
        else:
            uf[j] = i
            rank[i] += 1


for s in range(N):
    if s % 10000 == 0:
        print('scan %i, size=%i' % (s+1, len(set(uf.values()))))
    for vn in nb(graph[s]):
        if vn in uf:
            merge(gn[s], vn)

for i in uf:
    find(i)
print('DONE, cluster size=%i' % len(set(uf.values())))    