from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Node:
    value: int
    previous: Node | None = None
    next: Node | None = None

@dataclass
class DoublyLinkedList:
    length: int = 0
    head: Node | None = None

    def prepend(self, node: Node) -> None:
        self.length += 1

        if not self.head:
            self.head = node
            return

        self.head.previous = node
        node.next = self.head 
        self.head = node

        return

    def append(self, node: Node) -> None:
        current_node = self.head

        if not current_node:
            return self.prepend(node)

        while True:
            if current_node.next:
                current_node = current_node.next 
            else:
                current_node.next = node 
                node.previous = current_node
                return

    def insert_at(self, node: Node, position: int) -> None:
        if position == 0:
            return self.prepend(node)

        if self.length < position:
            raise IndexError("Index out of bounds")

        if self.length == position:
            return self.append(node)

        current_node = self.head
        for _ in range(position):
            if current_node.next:
                current_node = current_node.next            
            else:
                self.length += 1
                node.previous = current_node 
                current_node.next = node
                return 

        self.length += 1
        node.previous = current_node.previous
        current_node.previous = node
        node.next = current_node 
        node.previous.next = node

        return

    def print_node_at_position(self, position: int) -> None:
        if not self.head:
            raise IndexError("Empty DoublyLinkedList")
        
        if position == 0:
            print(self.head.value)
            return
            
        if position >= self.length:
            raise IndexError("Index out of bounds")

        current_node = self.head
        for _ in range(position):
            current_node = current_node.next

        if current_node:
            print(current_node.value)
        else:
            raise IndexError("Index out of bounds")

if __name__ == "__main__":
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)

    dll = DoublyLinkedList()
    dll.prepend(a)
    dll.prepend(b)
    dll.prepend(c)
    dll.insert_at(d, 2) # 3 -> 2 -> 4 -> 1
    # print(dll.length)

    dll.print_node_at_position(0)
    dll.print_node_at_position(1)
    dll.print_node_at_position(2)
    dll.print_node_at_position(3)
