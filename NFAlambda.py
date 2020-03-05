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
print(l)
def evalueaza(sc,cuv,sol):
    if cuv=="":
        return fin.intersection(sol)!=set()
    else:
        aux = set()
        for x in sol:
            if cuv[0] in l[x]:
                aux=aux.union(l[x][cuv[0]])
            if 'la' in l[x]:
                aux = aux.union(l[x]['la'])
        return evalueaza(sc,cuv[1:],aux)
a = set()
a.add(q0)
print(evalueaza(0,'bbbb',a))