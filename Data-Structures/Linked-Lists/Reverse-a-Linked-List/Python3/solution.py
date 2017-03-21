"""
 Reverse a linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def Reverse(head):
    if (head == None):
        return None
    
    if (head.next == None):
        return head
    
    rest = Reverse(head.next)
    
    head.next.next = head
    head.next = None
    
    return rest
