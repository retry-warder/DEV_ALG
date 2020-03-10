import SingleArray as SA


class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

    def get_item(self):
        return self.item

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


class PriorityQueue:

    def __init__(self):
        self.head = None
        self.queue = SA.SingleArray()

    def enqueue(self, node):
        if self.size() == 0:
            self.queue.add(node)
        else:
            for x in range(0, self.size()):
                if node.get_next() >= self.queue.get(x).get_next():
                    if x == (self.size() - 1):
                        self.queue.append(node, x + 1)
                    else:
                        continue
                else:
                    self.queue.append(node, x)
                    return True
        self.head = self.queue.get(0)

    def dequeue(self):
        if self.isEmpty():
            return None
        item = self.head.get_item()
        self.queue.remove(0)
        if not self.isEmpty():
            self.head = self.queue.get(0)
        else:
            self.head = None
        return item

    def show(self):
        for x in range(0, self.queue.size()):
            print(str(self.queue.get(x).get_item()) + " - " + str(self.queue.get(x).get_next()))
        print("----------------------------------------------")

    def size(self):
        return self.queue.size()

    def isEmpty(self):
        return self.queue.size() == 0


if __name__ == '__main__':
    pQueue = PriorityQueue()
    node1 = Node("C", 3)
    node2 = Node("B", 2)
    node3 = Node("A", 1)
    node4 = Node("Z", 26)
    node5 = Node("Y", 25)
    node6 = Node("L", 12)

    pQueue.enqueue(node1)
    pQueue.enqueue(node2)
    pQueue.enqueue(node3)
    pQueue.enqueue(node4)
    pQueue.enqueue(node5)
    pQueue.enqueue(node6)
    pQueue.show()
    print("****" + pQueue.dequeue() + "****")
    print("****" + pQueue.dequeue() + "****")
    pQueue.show()
