class Node:
    def __init__(self, data):
        self.data = data
        self.link = None
        

class Stack: #堆疊
    def __init__(self):
        self.top = None

    def add_node(self, item):
        new_node = Node(item) #產生一個新節點
        new_node.link = self.top 
        self.top = new_node #新節點成為top節點

    def __str__(self):
        elements = []
        current = self.top
        while current:
            elements.append(str(current.data))
            current = current.link
        return " -> ".join(elements)
    
    def pop(self):
        if self.is_empty(): #判斷鏈結堆疊「是否為空」
            raise Exception("STACK_EMPTY")
        node_to_remove = self.top #指標指向頂端的節點
        item = node_to_remove.data #取出頂端資料
        self.top = self.top.link #頂端指標Top改指向第二個節點
        del node_to_remove
        return item
    
    def is_empty(self):
        return self.top is None

#堆疊範例
stack = Stack()
print("執行堆疊新增範利:")
stack.add_node(1)
stack.add_node(2)
stack.add_node(3)
print(stack) #輸出: 3 -> 2 -> 1

print("執行堆疊刪除範例:")
print(stack.pop()) #輸出: 3
print(stack) #輸出: 2 -> 1


class Queue: #佇列
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def add_queue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.link = new_node
            self.rear = new_node

    def del_queue(self):
        if self.is_empty():
            raise Exception("Queue_Empty")
        else:
            node_to_remove = self.front #先利用一個指標指向前端節點
            item = node_to_remove.data #取出前端的資料
            self.front = self.front.link #前端的指標front至下一個節點
            if self.front is None:
                self.rear = None
            del node_to_remove
            return item

    def __str__(self):
        elements = []
        current = self.front
        while current:
            elements.append(str(current.data))
            current = current.link
        return " -> ".join(elements)
    
#佇列範例
queue = Queue()
print("執行佇列新增操作:")
queue.add_queue(10)
queue.add_queue(20)
queue.add_queue(30)
print(queue)  # 輸出: 10 -> 20 -> 30

print("執行佇列刪除操作:")
print(queue.del_queue())  # 輸出: 10
print(queue)  # 輸出: 20 -> 30