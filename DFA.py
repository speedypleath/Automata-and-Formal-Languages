f = open("date.in")
n = int(f.readline())
char = [x for x in f.readline().split()]
q0 = int(f.readline())
fin = [int(x) for x in f.readline().split()]
l=[{} for i in range(n)]
st = f.readline()
while st!="":
    (a,b,c)=[x for x in st.split()]
    l[int(a)][b]=int(c)
    st=f.readline()

def evalueaza(sc,cuv):
    if cuv=="":
        return sc in fin
    else:
        if cuv[0] in l[sc]:
            sc = l[sc][cuv[0]]
            return evalueaza(sc,cuv[1:])
        else:
            return False
print(evalueaza(0,'bacyaab'))