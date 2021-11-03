f = open("date.in")
import queue
neterm = set([x for x in f.readline().split()])
term = set([x for x in f.readline().split()])
gram = {}
print(neterm)
st = f.readline()
while st:
    if st[0] not in gram:
        gram[st[0]] = []
    gram[st[0]].append(st[2:-1])
    st = f.readline()
ok = 1
print(gram)
while ok: #pas1
    ok = 0
    aux = gram.copy()
    for x in gram:
        if '$' in gram[x]:
            ok = 1
            if len(gram[x]) == 1:
                del aux[x]
                neterm.remove(x)
                for i in aux:
                    for j in range(len(i)):
                        if aux[i][j] == x:
                            aux[i][j] = '$'
                        elif x in aux[i][j]:
                            aux[i][j] = aux[i][j].replace(x,'')
            else:
                aux[x].remove('$')
                for i in aux:
                    for j in range(len(i)):
                        if x in aux[i][j]:
                            k = aux[i][j].find(x)
                            while k != -1:
                                if aux[i][j][:k]+aux[i][j][k+1:] not in aux[i]:
                                    aux[i].append(aux[i][j][:k]+aux[i][j][k+1:])
                                k = aux[i][j].find(x,k+1)

    gram = aux
print(gram) #pas2
for x in gram:
    for y in range(len(gram[x])):
        if len(gram[x][y]) == 1 and gram[x][y][0] in neterm:
            if x != gram[x][y]:
                for k in gram[gram[x][y]]:
                    if k not in gram[x]:
                        gram[x].append(k)
            gram[x].remove(gram[x][y])

print(gram)

viz = {x:0 for x in neterm}
print(viz)
rem = set()
for x in gram: #pas 3
    q = queue.Queue()
    viz = {x:0 for x in neterm}
    q.put(x)
    viz[x] = 1
    while not q.empty():
        ok = 1
        for y in range(len(gram[x])):
            if neterm.intersection(set(gram[x][y])) == set():
                ok = 0
                break
            else:
                for k in neterm.intersection(set(gram[x][y])):
                    if not viz[k]:
                        viz[k] = 1
                        q.put(k)
            q.get()
        if not ok:
            break
    else:
        rem.add(x)
for x in rem:
    del gram[x]
    neterm.remove(x)
    for i in gram:
        for j in range(len(gram[i])):
            gram[i][j] = gram[i][j].replace(x,'')
q = queue.Queue()
viz = {x:0 for x in neterm}
viz['S'] = 1
q.put('S')
while not q.empty():
    x = q.get()
    for y in range(len(gram[x])):
        for k in neterm.intersection(set(gram[x][y])):
            if not viz[k]:
                viz[k] = 1
                q.put(k)
for x in viz:
    if not viz[x]:
        del gram[x]
        neterm.remove(x)

rem = set()
for x in gram: #pas 4
    for y in range(len(gram[x])):
        aux = term.intersection(set(gram[x][y]))
        if aux != set() and neterm.intersection(set(gram[x][y])) != set():
            for k in aux:
                gram[x][y] = gram[x][y].replace(k,k.upper())
                rem.add(k.upper())
for x in rem:
    gram[x] = x.lower()

c = 1
d = {}
ok = 1
while ok:
    ok = 0
    for x in gram:
        aux = gram.copy()
        for y in range(len(gram[x])):
            if len(gram[x][y])>2:
                if gram[x][y][1:] not in d:
                    aux[str(c)] = gram[x][y][1:3]
                    d[gram[x][y][1:]] = str(c)
                    gram[x][y] = gram[x][y][0] + str(c)
                    c += 1
                    ok = 1
                else:
                    gram[x][y] = gram[x][y][0] + d[gram[x][y][1:]]
        gram = aux
print(gram)
