f = open("date.in")
n = int(f.readline())
char = [x for x in f.readline().split()]
q0 = int(f.readline())
fin = [int(x) for x in f.readline().split()]
l=[{} for i in range(n)]
st = f.readline()
while st!="":
    (a,b,c)=[x for x in st.split()]
    if b not in l[int(a)]:
        l[int(a)][b]=set()
    l[int(a)][b].add(int(c))
    st=f.readline()
print(l)
def evalueaza(sc,cuv):
    if cuv=="":
        return sc in fin
    else:
        if cuv[0] in l[sc]:
            aux = set()
            for x in l[sc][cuv[0]]:
                aux=aux.union(l[x][cuv[0]])
                print("da",l[x][cuv[0]],x)
            print(aux)
            return evalueaza(sc,cuv[1:])
        else:
            return False
print(evalueaza(0,'aab'))