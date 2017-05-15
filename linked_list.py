class Node:
    def __init__(self, value=None, link=None):
        self.value = value
        self.link = link

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, cur_node=None, head=None):
        self.cur_node = cur_node
        self.head = head

    def add(self, value):
        new_node = Node()
        new_node.value = value
        if self.cur_node is not None:
            self.cur_node.link = new_node
        else:
            self.head = new_node
        self.cur_node = new_node

    def lprint(self):
        node = self.head
        while node:
            print(node.value)
            node = node.link

    def reverse(self):
        old_node = None
        node = self.head
        while node:
            if node == self.head:
                next_node = node.link
                old_node = node
                node.link = None
                node = next_node
            else:
                next_node = node.link
                node.link = old_node
                old_node = node
                node = next_node
        self.head = old_node


def main():
    new_list = LinkedList()
    for i in range(1, 10):
        new_list.add(i)
    new_list.lprint()
    new_list.reverse()
    new_list.lprint()


if __name__ == '__main__':
    main()
