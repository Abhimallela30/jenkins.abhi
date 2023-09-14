'''
m=3
n=4
a=[]
for i in range(m):
    l=[]
    for j in range(n):
        k=int(input())
        l.append(k)
    a.append(l)
print(a)

for i in range(m):
    for j in range(n):
        if a[i][j]==0:
            for k in range(n):
                if a[i][k]!=0:
                    a[i][k]=-1
            for k in range(m):
                if a[k][j]!=0:
                    a[k][j]=-1
for i in range(m):
    for j in range(n):
        if a[i][j]==-1:
            a[i][j]=0
print(a)
for i in range(m):
    for j in range(n):
        print(a[i][j],end=" ")
print()



class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def listlength(self):
        length=0
        cn=self.head
        while cn is not None:
            length+=1
            cn=cn.next
        return length
    def deletenode(self):
        ln=self.head
        while ln.next is not None:
            previousnode=ln
            ln=ln.next

        previousnode.next=None

    def deletemiddle(self,pos):
        ln=self.head
        cs=0
        while cs==pos:
            temp=ln.next
            cn.next=temp
        
        

    def insertHead(self,nn):
        temp=self.head
        self.head=nn
        self.head.next=temp
        del temp
    def insertMiddle(self,nn,pos):
        if pos<0 or pos>self.listlength():
            print("Invalid position")
            return
        elif pos==0:
            self.insertHead(nn)
            return
        cn=self.head
        cp=0
        while True:
            if cp==pos:
                previousnode.next=nn
                nn.next=cn
                break
            previousnode=cn
            cn=cn.next
            cp+=1
    def insertEnd(self,nn):
        if self.head is None:
            self.head=nn
        else:
            ln=self.head
            while True:
                if ln.next==None:
                    break
                ln=ln.next
            ln.next=nn
    def pl(self):
        cn=self.head
        while True:
            if cn is None:
                break
            print(cn.data)
            cn=cn.next

fn=Node("a")
sn=Node("b")
tn=Node("c")
m=Node("d")
n=Node("e")
ll=LinkedList()
ll.insertEnd(fn)
ll.insertEnd(sn)
ll.insertHead(tn)
ll.insertMiddle(m,2)
ll.insertMiddle(n,3)

#ll.deletenode()
ll.pl()


'''
m=3
n=4
a=[]
for i in range(m):
    l=[]
    for j in range(n):
        k=int(input())
        l.append(k)
    a.append(l)
print(a)
l=[0]*m
l1=[0]*n
for i in range(m):
    for j in range(n):
        if a[i][j]==0:
            l[i]=1
            l1[j]=1
print(l,l1)
for i in range(m):
    for j in range(n):
        if l[i]==1 or l1[j]==1:
            a[i][j]=0
print(a)
        














            
