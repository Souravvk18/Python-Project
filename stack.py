from collections import deque
# stack=deque()
class stack:
	def __init__(self):
		self.container =deque()
	def push(self,val):
		self.container.append(val)
	def pop(self):
		return self.container.pop()
	def peek(self):
		return self.container[-1]
	def is_empty(self):
		return len(self.container)==0
	def size(self):
		return len(self.container)
s= stack()
s.push(5)
s.push(500)
s.push(300)
# print(s.peek())
s.push(100)
# print(s.peek())
# print(s.is_empty())
# print (s.pop())
# print (s.pop())
# print (s.pop())
# print (s.pop())
print (s.size())


