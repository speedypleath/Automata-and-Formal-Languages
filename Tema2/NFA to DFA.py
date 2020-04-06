import queue
f = open("date2.in")
n = int(f.readline())
char = [x for x in f.readline().split()]
q0 = int(f.readline())
fin = {int(x) for x in f.readline().split()}
l=[{} for i in range(n)]
for i in range(n):
    for x in char:
        l[i][x]=set()
st = f.readline()
while st!="":
    (a,b,c)=[x for x in st.split()]
    if b not in l[int(a)]:
        l[int(a)][b]=set()
    l[int(a)][b].add(int(c))
    st=f.readline()
c=queue.Queue()
aux = set()
for x in char:
    aux = aux.union(l[q0][x])
c.put(tuple(aux))
viz = [tuple([q0]),tuple(aux)]
while not c.empty(): #pasul 1-eliminarea nedeterminismului
    a = c.get()
    for y in char:
        aux = set()
        for x in a:
            aux=aux.union(l[x][y])
        aux = tuple(aux)
        if aux not in viz:
            c.put(aux)
            viz.append(aux)
new_fin=[]
for i in range(len(viz)): #pasul 2-stari finale
    for x in viz[i]:
        if x in fin:
            new_fin.append(i)
print(new_fin)
dfa = [{} for i in range(len(viz))]
for i in range(len(viz)): #pasul 3-redenumire stari
    for x in char:
        aux = set()
        for k in viz[i]:
            aux = aux.union(l[k][x])
        if aux!=set():
            dfa[i][x]=viz.index(tuple(aux))
print(dfa)
