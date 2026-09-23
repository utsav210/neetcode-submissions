class Node:
    def __init__(self,val,next_node: Optional['Node'] = None):
        self.val = val
        self.next = next_node
class LinkedList:
    
    def __init__(self):
        self.head = None
        

    def get(self, index: int) -> int:
        curr = self.head
        curr_index = 0
        while curr:
            if curr_index == index:
                return curr.val
            curr = curr.next
            curr_index += 1
        return -1

    def insertHead(self, val: int) -> None:
        curr = self.head
        self.head = Node(val,next_node=curr)

    def insertTail(self, val: int) -> None:
        
        if self.head is None:
            self.head = Node(val)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(val)

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False
        if index == 0:
            self.head = self.head.next
            return True

        curr = self.head
        curr_idx = 1
        while curr.next:
            if curr_idx == index:
                temp = curr.next.next
                curr.next = temp
                return True
            curr_idx += 1
            curr = curr.next
        return False

    def getValues(self) -> List[int]:
        l = list()
        curr = self.head
        while curr:
            l.append(curr.val)
            curr = curr.next
        return l