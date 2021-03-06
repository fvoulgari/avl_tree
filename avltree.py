import random
import datetime



class Node():
    def __init__(self, key,card,payment,day,counter):
        self.key = key # node's key
        self.left = None # node's left child
        self.right = None # node's right child
        self.height = 0 # node's height = 1 + max(-1, -1)
        self.day=[day]
        self.payment=payment;
        self.card=card
        self.counter=counter

    def __str__(self):
        return str(self.key)
     # return f'{str(self.key)} h={self.height}'
class AVLtree():
 # ---
 # Search for a node with key
 #---------------------------
    def search(self, root, key,card,day,payent):
        while(root):
            if(root.card==card):
                root.payment +=payment
                root.day.append(day)
                root.counter +=1
                return True
            if(key>root.key):
                return tree.search(root.right,key,card,day,payment)
            elif(key<=root.key):
                return tree.search(root.left,key,card,day,payment)
        return False
    def insert(self, root, key,card,payment,day):
         if not root:
             return Node(key,card,payment,day,1)
         # Insert key to the left subtree
         elif( key <= root.key):

             root.left = self.insert(root.left, key,card,payment,day)
         # Insert key to the right subtree
         elif key > root.key:

             root.right = self.insert(root.right, key,card,payment,day)

         # rebalance tree if needed

        # root = self.rebalance(root)



         return self.rebalance(root)


    def rebalance(self, root):
 # Step 2 - Update the height
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

 # Step 3 - Get the balance factor
        balance = self.getBalance(root)

        if balance > 1:
            if self.getBalance(root.left) < 0:
                root.left = self.leftRotate(root.left)

            return self.rightRotate(root)
        if balance < -1:
            if self.getBalance(root.right) > 0:
                root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        return root
    def leftRotate(self, x):

        y = x.right
        B = y.left

        y.left = x
        x.right = B

        x.height = 1 + max(self.getHeight(x.left),self.getHeight(x.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))
        return y

    def rightRotate(self, x):
        y = x.left
        B = y.right

        y.right = x
        x.left = B
        x.height = 1 + max(self.getHeight(x.left),self.getHeight(x.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))
        return y
    def getHeight(self, root):

        if not root: return -1
        return root.height
    def getBalance(self, root):

        if not root: return 0
        return self.getHeight(root.left) - self.getHeight(root.right)
    def inOrder(self, root, rv):
         if not root: return
         self.inOrder(root.left, rv)
         z=(root.card,root.payment,root.day,root.key,root.counter)
         rv.append(z)
         self.inOrder(root.right, rv)


def cardgen():

    card=list("1234567890123456")
    temp1=random.randint(0,15)
    temp2=random.randint(0,15)
    while(temp1==temp2):

        temp2=random.randint(0,15)

    temp3=random.randint(0,15)
    while(temp1==temp3 or temp2==temp3):
        temp3=random.randint(0,15)

    temp4=random.randint(0,15)
    while(temp4==temp2 or temp4==temp3 or temp4==temp1):

        temp4=random.randint(0,15)



    card[temp1]="X"
    card[temp2]="Y"
    card[temp3]="Z"
    card[temp4]="W"
    temp="".join(card)
    return temp


def keygen(word):
    z = 33
    code = 0
    for c in word:
        code = z * code + ord(c)

    return code%1000000

def daygen():
    x=""
    temp=random.randint(0,5)
    if(temp==0):
        x="Mon"
    if(temp==1):
        x="Tue"
    if(temp==2):
        x="Wed"
    if(temp==3):
        x="Thu"
    if(temp==4):
        x="Fri"
    if(temp==5):
        x="Sat"

    return x




if __name__ == "__main__":
    random.seed(1468793)

    data = [3, 1, 2] # LR

    tree = AVLtree()
    root = None
    for i in range(1000000):
        card=cardgen()

        payment=random.randint(10,100)

        day=daygen()
        key=keygen(card)
        if not (tree.search(root,key,card,day,payment)):
            root = tree.insert(root, key,card,payment,day)


 # inOrder traversal
    inot = []
    temp=0
    tree.inOrder(root, inot)
    for i in inot :
        if(i[4]>temp):
            temp=i[4]
            name=i[0]
    print("the most visits are ",temp,"from",name )
    temp=0
    for i in inot :
        if(i[1]>temp):
            temp=i[1]
            name=i[0]
    print( temp,"euros from",name)
    temp=0
    temp1=0
    temp2=0
    temp3=0

    temp4=0
    temp5=0
    maxfind=0
    for i in inot:
        for e in i[2]:
            if(e=="Mon"):
                temp+=1

            if(e=="Tue"):
                temp1+=1
            if(e=="Wed"):
                temp2+=1
            if(e=="Thu"):
                temp3+=1
            if(e=="Fri"):
                temp4+=1
            if(e=="Sat"):
                temp5+=1


if (temp>max(temp1,temp2,temp3,temp4,temp5)):
    name="Mon"
    maxfind=temp
if (temp1>max(temp,temp2,temp3,temp4,temp5)):
    name="Tue"
    maxfind=temp1
if (temp2>max(temp1,temp,temp3,temp4,temp5)):
    name="Wed"
    maxfind=temp2
if (temp3>max(temp1,temp2,temp,temp4,temp5)):
    name="Tue"
    maxfind=temp3
if (temp4>max(temp1,temp2,temp3,temp,temp5)):
    name="Fri"
    maxfind=temp4
if (temp5>max(temp1,temp2,temp3,temp4,temp)):
    name="Sat"
    maxfind=temp5

print(name,maxfind)

    #tree.display(root)
 # tree.save(root)
