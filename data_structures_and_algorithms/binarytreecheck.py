class node:
    def __init__(self,value):
        self.value=value
        self.left_child=None
        self.right_child=None


    def _print_tree(self,trr):
        if trr.left_child:
            self._print_tree(trr.left_child)

        lis.append(trr.value)
                
        if trr.right_child:
            self._print_tree(trr.right_child)
        return lis

lis=[]            
            
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
arr=x._print_tree(x)
print(arr)

if sorted(arr)==arr:
    print("Yeah Binary tree")
else:
    print("Naaaaah!")

			
