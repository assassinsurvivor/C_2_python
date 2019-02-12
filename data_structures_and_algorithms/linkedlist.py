class node:
    def __init__(self,value):
        self.value=value
        self.child=None
        self.parent=None

class linkedlist:

    def __init__(self):
        self.root=None


    def list(self,value):
        if self.root==None:
            self.root=node(value)

        else:
            self._list(self.root,value)

    def _list(self,current,value):

        if current.child==None:
            current.child=node(value)
            current.child.parent=current
        else:
            self._list(current.child,value)

    def print_linkedlist(self):

        if self.root:
            return self._print_linkedlist(self.root)

    def _print_linkedlist(self,current):

        print(current.value)

        if current.child:
            return self._print_linkedlist(current.child)



x=linkedlist()
x.list(5)
x.list(15)
x.list(3)
x.list(7)
x.list(6)
x.list(11)

x.print_linkedlist()

        
        
            

        
