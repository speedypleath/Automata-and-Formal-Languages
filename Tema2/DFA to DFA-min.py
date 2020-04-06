import queue
f = open("date3.in")
n = int(f.readline())
char = [x for x in f.readline().split()]
q0 = int(f.readline())
fin = {int(x) for x in f.readline().split()}
l=[{} for i in range(n)]
st = f.readline()
while st!="":
    (a,b,c)=[x for x in st.split()]
    l[int(a)][b]=int(c)
    st=f.readline()
print(l)
adiacenta = [[True]*x for x in range(n)]
nefin = {x for x in range(n)} - fin
for x in fin:    #pasul 1-stari echivalente
    for y in nefin:
        adiacenta[max(x,y)][min(x,y)]=False
ok = True
while ok:
    ok = False
    for i in range(n):
        for j in range(i):
            for x in char:
                a = l[i][x]
                b = l[j][x]
                if a != b and adiacenta[max(a,b)][min(a,b)] is False:
                    ok = adiacenta[i][j]
                    adiacenta[i][j] = False

aux = [x for x in range(n-1,-1,-1)]

new = []
for x in aux:   #pasul2-gruparea starilor echivalente
    a = {x}
    for j in range(len(adiacenta[x])):
        if adiacenta[x][j]:
            a.add(j)
            aux.remove(j)
    new.append(a)

new = new[::-1]
m = len(new)
dfa_min = [{} for i in range(m)]
for i in range(m):
    for y in char:
        x = next(iter(new[i]))
        x = l[x][y]
        for j in range(m):
            if x in new[j]:
                dfa_min[i][y] = j

for i in range(m):    #pasul 3-stari finale,stare initiala
    if q0 in new[i]:
        new_q0 = i
        break
new_fin = set()
for i in range(m):
    if fin.intersection(new[i]):
        new_fin.add(i)
coada = queue.Queue(m)
for x in range(m):   #eliminarea starilor dead-end
    coada.put(x)
    viz = [False] * m
    viz[x] = True
    while not coada.empty():
        while not coada.empty():
            i = coada.get()
            for j in char:
                if j in dfa_min[i]:
                    if dfa_min[i][j] in new_fin:
                        break
                    if not viz[dfa_min[i][j]]:
                        coada.put(dfa_min[i][j])
                        viz[dfa_min[i][j]] = True
            else:
                dfa_min = dfa_min[:i] + dfa_min[i + 1:]
                delete = {}
                for k1 in dfa_min:
                    for k2 in k1:
                        if k1[k2] == i:
                            k1[k2] = None
coada = queue.Queue(m)
coada.put(q0)
viz = [False]*m
viz[q0] = True
while not coada.empty():  #pasul 5-eliminarea starilor neaccesibile
    i = coada.get()
    for j in char:
        if j in dfa_min[i] and dfa_min[i][j]:
            if not viz[dfa_min[i][j]]:
                coada.put(dfa_min[i][j])
                viz[dfa_min[i][j]] = True
for i in range(m):
    if not viz[i]:
        dfa_min = dfa_min[:i] + dfa_min[i + 1:]
