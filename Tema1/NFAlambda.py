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
def evalueaza(cuv,states):
    new_states = states
    old_states = set()
    while old_states!=new_states:
        old_states=new_states
        for x in old_states:
            if 'la' in l[x]:
                new_states = new_states.union(l[x]['la'])
    if cuv=="":
        return fin.intersection(new_states)!=set()
    else:
        aux = set()
        for x in new_states:
            if cuv[0] in l[x]:
                aux=aux.union(l[x][cuv[0]])
        return evalueaza(cuv[1:],aux)
a = set()
a.add(q0)
print(evalueaza('abyyxyx',a))
