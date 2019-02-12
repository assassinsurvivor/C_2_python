class node:

    def __init__(self,value):
        self.value=value
        self.left_child=None
        self.right_child=None


def diagonal_elements_bst(tree):

    stack=[]
    stack.append(tree)
    stack.append(None)
    while(len(stack)!=0):
        
        temp=stack.pop(0)
        if(temp==None):
            print("")
            stack.append(None)
            temp=stack.pop(0)
            if temp==None:
                break




        while(temp!=None):
            if (temp.left_child):
                stack.append(temp.left_child)

            print(temp.value,"",end="")
            temp=temp.right_child
        



x=node(4)
y=node(2)
z=node(7)
a=node(1)
b=node(5)
c=node(6)
d=node(10)
e=node(11)
f=node(14)
g=node(12)
h=node(17)
i=node(16)


x.left_child=y
x.right_child=z
y.left_child=a
z.left_child=b
z.right_child=d
b.right_child=c
d.right_child=e
e.right_child=f
f.left_child=g
f.right_child=h
h.left_child=i

diagonal_elements_bst(x)

