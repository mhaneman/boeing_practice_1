class MyNode:
    def __init__(self, value, prev):
        self.value = value
        self.prev = prev


class MyStack:
    def __init__(self) -> None:
        self.head_node = None

    def push(self, value) -> None:
        if self.head_node is None:
            self.head_node = MyNode(value, None)
        else:
            new_node = MyNode(value, self.head_node)
            self.head_node = new_node

    def peak(self):
        # probably ask interviewer if they would like to see an error or None
        if self.head_node is None:
            raise ValueError("Stack is empty")

        return self.head_node.value

    def pop(self):
        if self.head_node is None:
            raise ValueError("Stack is empty")

        popped_value = self.head_node.value
        self.head_node = self.head_node.prev
        return popped_value
