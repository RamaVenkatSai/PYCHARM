class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class Linked_list:
    def __init__(self):
        self.head=node()
    def append(self,data):
        new_node=node(data)
        cur=self.head
        while cur.next!=None:
            cur=cur.next
        cur.next=new_node
        #new_node.next=self.head
    def display(self):
        cur_node=self.head
        while cur_node.next!=self.head:
            cur_node=cur_node.next
            print(cur_node.data)
        print("head is")
        print((cur_node.next).data)

    def last_node(self):
        curr_node = self.head
        while curr_node.next != None:
            curr_node = curr_node.next
        curr_node.next = self.head
    def delete(self):

        cur_node = self.head
        i=50
        while i>0:
            #c=cur_node
            #print(cur_node.data)
            #print((cur_node.next).data)
            #print((((cur_node.next).next).next).data)
            (cur_node.next).next = ((cur_node.next).next).next
            cur_node=cur_node.next
            if(cur_node.next==self.head):
                self.head=(self.head).next

            #c.next=None
           # print(cur_node.data)
            i-=1




l=Linked_list()
for i in range(1,101):
    l.append(i)
l.last_node()
l.display()
l.delete()
print("hai")
l.display()
#print((l.head.next).next.data)

#curr_node=l.head
#while curr_node.next!=l.head:
    #print(curr_node.data)
    #curr_node=curr_node.next
#print(((curr_node.next).next).data)