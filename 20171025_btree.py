import sys
from bisect import bisect_right,insort, bisect_left


class BTree_Node:
	def __init__(self, flag = 0):
		self.keys = []
		self.pointers = [None]*4
		self.count = 0

	def insert_node(self, key, root_flag=True):
		if root_flag == True:
			node = self.insert_node(key, False)
			if node != None:
				root = BTree_Node()
				root.keys.insert(0, node.keys[0])
				root.pointers[0] = self
				root.count = root.count + 1
				root.pointers[1] = node
				return root
			else:
				return self

		else:
			
			if self.pointers[0] == None:
				self.count = self.count + 1
				insort(self.keys, key)
				if self.count < 4:
					return None
				else:
					sib_node = BTree_Node()
					sib_node.keys = []
					l_index = self.count/2
					r_index = self.count
					temp_keys = self.keys[l_index:r_index]
					sib_node.keys += temp_keys
					sib_node.count = r_index - l_index + 1
					self.keys = self.keys[0:l_index]
					self.count = l_index + 1
					
					sib_node.pointers[3] = self.pointers[3]
					self.pointers[3] = sib_node
					return sib_node
			
			else:
				index = bisect_right(self.keys, key)
				node = self.pointers[index].insert_node(key, False)
				if node == None:
					return None
				elif self.count < 4:
					new_key = node.keys[0]
					index = bisect_right(self.keys, new_key)
					self.keys.insert(insert, new_key)
					self.count = self.count + 1
					self.pointers.insert(index+1, node)
					self.pointers.remove(None)
				else:
					index = 0
					sib_node = Node()
					temp = self.pointers
					while index < 4 and node.keys[0] > self.pointers[index].keys[0]:
						index = index + 1
					temp.insert(index, node)
					l_ind = 1 + self.count/2
					r_ind = 2 + self.count
					self.pointers[0:l_ind] = temp[0:l_ind]
					self.keys = []
					sib_node.pointers[0:r_ind-l_ind] = temp[l_ind:r_ind]
					for i in range(1, l_ind):
						self.keys.append(self.pointers[i].keys[0])
					for j in range(l_ind, 4):
						self.pointers[j] = None
					for k in range(1, r_ind-l_ind):
						sib_node.keys.append(sib_node.pointers[k].keys[0])
					self.count = l_ind - 1
					sib_node.count = len(sib_node.keys)
					#print self.count, sib_node.count
					return sib_node
		return

	def print_tree(self):
		if self == None:
			return
		print(self.keys, self.count)

		if self.pointers[0] == None:
			return
		for i in range(4):
			self.pointers[i].print_tree()


file = sys.argv[1]
root = BTree_Node()
lines = [line.rstrip() for line in open(file, 'r')]
root.print_tree()
for line in lines:
	query = line.split(" ")
	# if(query[0] == "FIND"):
	# 	val = query[1]

	if(query[0] == 'INSERT'):
		val = int(query[1])
		root = root.insert_node(val)
		root.print_tree()
	# if(query[0] == "COUNT"):
	# 	val = query[1]

	# if(query[0] == "RANGE"):
	# 	val = query[1]

