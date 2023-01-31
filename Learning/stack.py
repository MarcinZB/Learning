# Zastosowanie stosów
# historia przeglądania w przeglądarce
#operacja "Cofnij" w edytorze tekstu


# Stworzenie stosu
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
        
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)

# Dodanie elementów do stosu
stack = Stack()
stack.push("RED")
stack.push("Green")
stack.push("Yellow")
stack.push("Blue")

print(stack.items)

# Zdjęcie elementu metoda pop
stack.pop()
print(stack.items)

#Sprawdzenie czy stos jest pusty
print(stack.isEmpty())

#
print(stack.peek())

#wielkość stosu
print(stack.size())


