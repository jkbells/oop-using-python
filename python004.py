# linklist in python


class listnode:
    def _init_(self,data):
        self.data = data
        self.next = none

node_1 = listnode(3)

print (node_1.data)
print (node_1.next)

node_2 = listnode(5)

node_1.next = node_2
print (node_1.data)
print (node_1.next.data)

node_3 = listnode(17)
node_2.next = node_3
print (node_1.next.next.data)

node_3.next = listnode(55)
print (node_1.next.next.next.data)
        
        
