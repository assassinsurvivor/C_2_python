class node:
    def __init__(self,value=None):

        self.value=value
        self.left_child=None
        self.right_child=None





def bfs (nodee,value):
    queue=[nodee]
    
    while(len(queue)>0):
        temp=queue.pop(0)
        
        if (temp.value==value):
            return True
        else:
            print(temp.value)
            if temp.left_child:
                queue.append(temp.left_child)
            if temp.right_child:
                queue.append(temp.right_child)
    return False




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

print(bfs(x,16))

                

    
