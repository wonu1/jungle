# 링크드리스트 - 에디터 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1406
import sys
input = sys.stdin.readline
result = []

class Node:
    def __init__(abab, data):
        abab.data = data
        abab.next = None
        abab.prev = None


class LinkedList:



    def __init__(self):
        self.head = Node('')
        self.tail = Node('')

        self.head.next = self.tail
        self.tail.prev = self.head
        self.cursor = self.head

    def append(self, data):
        new_node = Node(data)

        new_node.next = self.cursor.next
        new_node.prev = self.cursor

        self.cursor.next = new_node
        new_node.next.prev = new_node

        self.cursor = self.cursor.next

    
    def pre(self):
        if self.cursor != self.head:
            self.cursor = self.cursor.prev
    
    def daum(self):
        if self.cursor.next != self.tail:
            self.cursor = self.cursor.next

    
    # def delete(self):
    #     if self.cursor != self.head:
    #         self.cursor.prev.next = self.cursor.next
    #         self.cursor.next.prev = self.cursor.prev

    #         self.cursor = self.cursor.prev
    def delete(self):
        if self.cursor != self.head:
            left = self.cursor.prev
            right = self.cursor.next

            left.next = right
            right.prev = left

            self.cursor = left

    def show(self):
        current = self.head.next
        while current != self.tail:
            result.append(current.data)
            # print(current.data,end = '')
            current = current.next

    

arr = input().rstrip()
Larr = LinkedList()
for i in arr:
    Larr.append(i)

N = int(input())


for i in range(N):
    command = []
    command = input().split()

    match command[0]:
         
        case 'L':
            Larr.pre()
        case 'D':
            Larr.daum()
        case 'B':
            Larr.delete()
        case 'P':
            Larr.append(command[1])

Larr.show()
print(''.join(result))