import sys
import math

S=[]
def rec(M,a,b,L):
    if a==b or len(L)==3:
        L.append(b)
        X=L.copy()
        S.append(X)
        return None

    L.append(a)
    
    for i in range(len(M[a])):
        if M[a][i] ==1 and i not in L:
            rec(M,i,b,L)
            L.pop()
    return None

P=[]
n, l, e = [int(i) for i in input().split()]

R=[ [ 0 for i in range(n)] for i in range(n) ]


for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    R[n1][n2]=1
    R[n2][n1]=1
for i in range(e):
    ei = int(input())  # the index of a gateway node
    P.append(ei)

# game loop
while True:
    si = int(input())  # The index of the node on which the Bobnet agent is positioned this turn
    Min=[]
    S=[]
    for i in P:
        
        rec(R,i,si,[])
    Min=sorted(S, key=len)
    
 




    R[Min[0][0]][Min[0][1]]=0
    print(Min[0][0],Min[0][1])