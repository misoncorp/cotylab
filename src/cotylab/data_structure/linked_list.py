class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)
    

class DoubledNode(Node):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.prev = None


class LinkedList:
    NODE_CLASS = Node
    DELIMITER = ' -> '

    def __init__(self, values=[]):
        self.head = None
        self.tail = None
        self.current = None
        self.insert_nodes(values)

    def insert_nodes(self, values):
        self.head = None
        self.tail = None
        for value in values:
            self.insert_node(value)
        self.go_to_head()
    
    def insert_node(self, value, after=True):
        node = self.NODE_CLASS(value)
        if self.current is None:
            self.head = node
            self.tail = node
            self.current = node
            return
        if after:
            node.next = self.current.next
            self.current.next = node
        else:
            prev = None
            _node = self.head
            while _node is not None:
                if _node == self.current:
                    break
                prev = _node
                _node = _node.next
            if prev is None:
                self.head = node
                node.next = self.current
            else:
                prev.next = node
                node.next = self.current
        self.current = node
    
    def delete_node(self, node):
        current_node = self.head
        prev_node = None
        while current_node is not None:
            if current_node == node:
                if prev_node is None:
                    self.head = current_node.next
                else:
                    prev_node.next = current_node.next
                del current_node
                return True
            prev_node = current_node
            current_node = current_node.next
        return False

    def next(self):
        if self.current == -1:
            self.current = self.head
        elif self.current is not None:
            self.current = self.current.next
        else:
            return None
        return self.current

    def set_current(self, node):
        self.current = node

    def go_to_head(self):
        self.set_current(self.head)

    def go_to_tail(self):
        self.set_current(self.tail)

    def __str__(self):
        values = []
        current_node = self.head
        while current_node is not None:
            values.append(str(current_node.value))
            current_node = current_node.next
        return self.DELIMITER.join(values)


class DoubledLinkedList(LinkedList):
    NODE_CLASS = DoubledNode
    DELIMITER = ' <-> '

    def prev(self):
        if self.current == -1:
            self.current = self.tail
        elif self.current is not None:
            self.current = self.current.prev
        else:
            return None
        return self.current


class CircularLinkedList(LinkedList):
    def next(self):
        current = super().next()
        if current is None:
            self.current = self.head
        return self.current
