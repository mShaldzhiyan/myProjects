class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    l1values = [l1.val]
    l2values = [l2.val]
    while (l1.next):
        l1 = l1.next
        l1values.append(l1.val)
    while (l2.next):
        l2 = l2.next
        l2values.append(l2.val)
    l1int = int(''.join([str(a) for a in l1values])[::-1])
    l2int = int(''.join([str(a) for a in l2values])[::-1])
    numberstr = list(map(int, str(l1int+l2int)))
    i = len(numberstr) - 1
    node = None
    while i >= 0:
        if i == 0:
            return (ListNode(numberstr[i], node))
        elif (i == len(numberstr) - 1):
            node = ListNode(numberstr[i])
        else:
            node = ListNode(numberstr[i], node)


    print(numberstr)

addTwoNumbers(ListNode(1,ListNode(2)), ListNode(3,ListNode(5,ListNode(6))))