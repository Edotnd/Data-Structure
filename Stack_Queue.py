# stack
class stack:
    def __init__(self):
        self.data = []
    
    def push(self, value):
        self.data.append(value)
    
    def pop(self):
        return self.data.pop()

    def __call__(self):
        if self.data == []:
            print("Is Empty")
        else:
            print(self.data)

stack1 = stack()
stack1.push(1)
stack1.push(2)
stack1.pop()
stack1()

# queue
class queue:
    def __init__(self):
        self.data = []
    
    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        return self.data.pop(0)
    
    def __call__(self):
        if self.data == []:
            print("Is Empty")
        else:
            print(self.data)

queue1 = queue()
queue1.enqueue(1)
queue1.enqueue(2)
queue1.dequeue()
queue1()