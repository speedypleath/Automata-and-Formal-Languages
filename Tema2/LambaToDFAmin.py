import queue
f = open("date.in")
n = int(f.readline())
char = [x for x in f.readline().split()]
q0 = int(f.readline())
fin = {int(x) for x in f.readline().split()}
l=[{} for i in range(n)]
st = f.readline()
while st!="":
    (a,b,c)=[x for x in st.split()]
    if b not in l[int(a)]:
        l[int(a)][b]=set()
    l[int(a)][b].add(int(c))
    st=f.readline()
def lambdatonfa(n,char,q0,fin,l):
    c=queue.Queue(n)
    inchidere=[{x} for x in range(n)]
    for i in range(n):  #pasul 1-lambda inchidere
        c.put(i)
        while not c.empty():
            aux = c.get()
            if '$'in l[aux]:
                for x in l[aux]['$']:
                    if x not in inchidere[i]:
                        inchidere[i].add(x)
                        c.put(x)
    nfa = [{} for i in range(n)]
    for x in char:   #pasul 2-functia de tranzitie
        for i in range(n):
            aux=set()
            nfa[i][x]=set()
            for j in inchidere[i]:
                if x in l[j]:
                    aux=aux.union(l[j][x])
            for j in aux:
                nfa[i][x]=nfa[i][x].union(inchidere[j])
    new_fin=set()
    new_fin=new_fin.union(fin)
    for i in range(n):  #pasul 3-stari finale
        for x in fin:
            if x in inchidere[i]:
                new_fin.add(i)
    id={}
    viz=[0]*n

    for i in range(n): #pasul 4-stari redundante
        for j in range(i+1,n):
            if nfa[i]==nfa[j]:
                if viz[i]==0:
                    viz[i]=viz[j]=1
                    id[i]={j}
                else:
                    for x in id:
                        if i in id[x]:
                            id[x].add(j)
    print(id)
    for k in id:
        for x in range(n):
            for i in char:
                for j in id[k]:
                    if j in nfa[x][i]:
                        nfa[x][i].remove(j)
                        nfa[x][i].add(k)
    k=0
    for i in id:
        for j in id[i]:
            nfa.remove(nfa[j-k])
            n-=1
            k+=1
    for i in range(n):
        for j in char:
            aux = set()
            for x in nfa[i][j]:
                x1 = x
                for a in id:
                    for b in id[a]:
                        if x>b:
                            x1 -= 1
                aux.add(x1)
            nfa[i][j]=aux
    fin = set()
    for i in new_fin:
        x = i
        for a in id:
            for b in id[a]:
                if i > b:
                    x -= 1
        fin.add(x)


    return  n,char,q0,fin,nfa

def nfatodfa(n,char,q0,fin,l):
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
    new_fin=set()
    for i in range(len(viz)): #pasul 2-stari finale
        for x in viz[i]:
            if x in fin:
                new_fin.add(i)

    dfa = [{} for i in range(len(viz))]
    for i in range(len(viz)): #pasul 3-redenumire stari
        for x in char:
            aux = set()
            for k in viz[i]:
                aux = aux.union(l[k][x])
            if aux!=set():
                dfa[i][x]=viz.index(tuple(aux))
    return  len(dfa),char,q0,fin,dfa

def dfatomin(n,char,q0,fin,l):
    adiacenta = [[True] * x for x in range(n)]
    nefin = {x for x in range(n)} - fin
    for x in fin:  # pasul 1-stari echivalente
        for y in nefin:
            adiacenta[max(x, y)][min(x, y)] = False
    ok = True
    while ok:
        ok = False
        for i in range(n):
            for j in range(i):
                for x in char:
                    a = l[i][x]
                    b = l[j][x]
                    if a != b and adiacenta[max(a, b)][min(a, b)] is False:
                        ok = adiacenta[i][j]
                        adiacenta[i][j] = False

    aux = [x for x in range(n - 1, -1, -1)]

    new = []
    for x in aux:  # pasul2-gruparea starilor echivalente
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

    for i in range(m):  # pasul 3-stari finale,stare initiala
        if q0 in new[i]:
            new_q0 = i
            break
    new_fin = set()
    for i in range(m):
        if fin.intersection(new[i]):
            new_fin.add(i)
    coada = queue.Queue(m)
    for x in range(m):  # pasul 4-eliminarea starilor dead-end
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
                    k = i
                    for i in range(len(dfa_min)):
                        for j in char:
                            if j in dfa_min[i] and dfa_min[i][j] == k:
                                dfa_min[i].pop(j)
                            if j in dfa_min[i] and dfa_min[i][j] > k:
                                dfa_min[i][j] -= 1

    coada = queue.Queue(m)
    coada.put(q0)
    viz = [False] * m
    viz[q0] = True
    while not coada.empty():  # pasul 5-eliminarea starilor neaccesibile
        i = coada.get()
        for j in char:
            if j in dfa_min[i] and dfa_min[i][j]:
                if not viz[dfa_min[i][j]]:
                    coada.put(dfa_min[i][j])
                    viz[dfa_min[i][j]] = True
    for i in range(m):
        if not viz[i]:
            dfa_min = dfa_min[:i] + dfa_min[i + 1:]
            for x in range(len(dfa_min)):
                for y in char:
                    if y in dfa_min[x] and dfa_min[x][y] and dfa_min[x][y] > i:
                        dfa_min[x][y] -= 1
    return len(dfa_min), char, q0, new_fin, dfa_min

n,char,q0,fin,l = lambdatonfa(n,char,q0,fin,l)
print(n,char,q0,fin,l)
n,char,q0,fin,l = nfatodfa(n,char,q0,fin,l)
print(n,char,q0,fin,l)
n,char,q0,fin,l = dfatomin(n,char,q0,fin,l)
print(n,char,q0,fin,l)
