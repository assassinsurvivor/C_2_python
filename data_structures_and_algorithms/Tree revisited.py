class node:
    def __init__(self,value):
        self.value=value
        self.left_child=None
        self.right_child=None
        self.parent=None


class bst:

    def __init__(self):
        self.root=None


    def insert(self,value):

        if self.root==None:
            self.root=node(value)


        else:
            self._insert(self.root,value)


    def _insert(self,current,value):
        if value<current.value:
            if current.left_child==None:
                current.left_child=node(value)
                current.left_child.parent=current
            else:
                self._insert(current.left_child,value)

        elif value>current.value:
            if current.right_child==None:
                current.right_child=node(value)
                current.right_child.parent=current
            else:
                self._insert(current.right_child,value)

        elif value==current.value:
            print("Err... The node already exists!")



    def find(self,value):
        if self.root==None:
            return None

        else:
            return self._find(self.root,value)


    def _find(self,current,value):

        if value==current.value:
            return True

        elif value<current.value and current.left_child!=None:
            return self._find(current.left_child,value)

        elif value>current.value and current.right_child!=None:
            return self._find(current.right_child,value)

        return False


    def search(self,value):
        if self.root==None:
            return None

        else:
            return self._search(self.root,value)


    def _search(self,current,value):

        if value==current.value:
            return current

        elif value<current.value and current.left_child!=None:
            return self._search(current.left_child,value)

        elif value>current.value and current.right_child!=None:
            return self._search(current.right_child,value)

        return False


    def getheight(self):

        if self.root==None:
            return 0
        else:
            return self._getheight(self.root,0)


    def _getheight(self,current,counter):

        if current==None:
            counter-=1
            return counter

        left_height=self._getheight(current.left_child,counter+1)
        right_height=self._getheight(current.right_child,counter+1)

        return max(left_height,right_height)



    def depth_of_node(self,value):

        if self.root==None:
            return 0

        else:
            return self._depthofnode(self.root,value,0)

    def _depthofnode(self,current,value,counter):

        if current.value==value:
            return counter

        elif value<current.value:
            return self._depthofnode(current.left_child,value,counter+1)

        elif value>current.value:
            return self._depthofnode(current.right_child,value,counter+1)

        return False

    def is_valid_balanced_bst(self):
        if self.root==None:
            print("No such Tree exists!")
        else:
            return self._is_valid_balanced_bst(self.root,0)

    def _is_valid_balanced_bst(self,curr,counter):

        left_bst=self._getheight(curr.left_child,0)
        right_bst=self._getheight(curr.right_child,0)

        return abs(left_bst-right_bst)


    def print_tree(self,way):

        if self.root==None:
            print("No tree exists!!!!!")
        elif way=="inorder":
            print("Inorder Traversal of tree is :")
            self._print_tree_inorder(self.root)

        elif way=="preorder":
            print("preorder Traversal of tree is :")
            self._print_tree_preorder(self.root)

        elif way=="postorder":
            print("postorder Traversal of tree is :")
            self._print_tree_postorder(self.root)

        

    def _print_tree_inorder(self,current):


        if current.left_child:
            self._print_tree_inorder(current.left_child)

        print(current.value)



        if current.right_child:
            self._print_tree_inorder(current.right_child)

    def _print_tree_preorder(self,current):


        

        print(current.value)


        if current.left_child:
            self._print_tree_preorder(current.left_child)

        if current.right_child:
            self._print_tree_preorder(current.right_child)


    def _print_tree_postorder(self,current):

        if current.left_child:
            self._print_tree_postorder(current.left_child)

        if current.right_child:
            self._print_tree_postorder(current.right_child)


        print(current.value)



    def delvalue(self,value):

        if self.root==None:
            print("No such tree exists")
        else:
            return self.delnode(self.search(value))


    def delnode(self,current):

        if current==None or self.search(current.value)==None:
            print("Node to be deleted doesn't exists!")
            return None
        if current.parent==None:
            self.root=None
            return None

        

        def totalchild(nodee):
            child=0
            if nodee.left_child: child+=1
            if nodee.right_child: child+=1
            return child

        def successor(node):
            res=node
            while res.left_child!=None:
                res=node.left_child
            return res

        total=totalchild(current)
        ancestor=current.parent

        if total==0:
            if ancestor.left_child==current:
                ancestor.left_child=None
            else:
                ancestor.right_child=None

        if total==1:
            if current.left_child:
                children=current.left_child
                
            else:
                children=current.right_child

            if ancestor.left_child==current:
                ancestor.left_child=children
            else:
                ancestor.right_child=children

            children.parent=ancestor

        if total==2:
            suc=successor(current.right_child)
            current.value=suc.value
            self.delnode(suc)


x=bst()
x.insert(4)
x.insert(2)
x.insert(1)
x.insert(7)
x.insert(5)
x.insert(6)
x.insert(9)
x.insert(11)
x.insert(14)
x.insert(12)
x.insert(17)
x.insert(16)
x.print_tree("inorder")
x.print_tree("preorder")
x.print_tree("postorder")
print(x.find(12))
print(x.find(25))
print(x.getheight())
print(x.depth_of_node(11))
t=(x.is_valid_balanced_bst())
if t==1 :
    print("The tree is a complete balance Binary search tree with difference :",t)
if t==0 :
    print("The tree is a Full balance Binary search tree with difference :",t)
else:
    print("The tree is a unbalanced Binary search tree with difference :",t)

print(x.search(6))

x.delvalue(1)
x.print_tree("inorder")
x.delvalue(5)
x.print_tree("inorder")
x.delvalue(14)
x.print_tree("inorder")
    


            
        
        
        






























            
                
                
            
