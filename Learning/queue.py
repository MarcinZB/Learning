
#Kolejka
class Queue(object ):
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)

# Dodawanie wartości do kolejki
queue = Queue()
queue.enqueue("RED")
queue.enqueue("Green")
queue.enqueue("Blue")
queue.enqueue("Orange")
queue.enqueue("Purple")

print(queue.items)

# Usuwanie wartości z kolejki 
queue.dequeue()
print(queue.items)