class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularLinckedList:
    def __init__ (self):
        self.last = None
        self.size = 0 

    def insert_back(self, value):
        # Comprobacion
        if self.last is None:
            self.last = Node(value)
            self.last.next = self.last
            self.size += 1
            return
        
        new_node = Node(value)
        new_node.next = self.last.next

        self.last.nest  = new_node
        self.last = self.last.next

        self.size += 1

    def insert_at(self, index, value):
        pass

    def search (self, value):
        pass
    def delete_front(self):

        if self.last is None:
            return
        if self.size ==1:
            self.last = None
        else: 
            self.last.next = self.last.next.next

        self.size -=1

    def insert_front(self, value):
        if self.last is None:
            self.last = None (value)
            self.last.next = self.last 
            self.size += 1 
            return
        
        new_node = Node(value)
        new_node.next = self.last.next

        self.last.next = new_node
        self.size += 1

    def print(self):
        if self.last is None:
            print ("Las lista esta vacia")
            return
        
        aux  = self.last.next
        while aux is not self.last:
            print(aux.value, end='->')
            aux = aux.next
            
        print(aux.value)
