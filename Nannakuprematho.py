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
    def display(self):
        cur_node=self.head
        while cur_node.next!=self.head:
            cur_node=cur_node.next
            print(cur_node.data)
        #print("head is")
        #print((cur_node.next).data)
        def last_node(self):
            curr_node = self.head
            while curr_node.next != None:
                curr_node = curr_node.next
            curr_node.next = self.head