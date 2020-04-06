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
print(nfa)
