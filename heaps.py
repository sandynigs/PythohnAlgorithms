class BinHeap:

	def __init__(self):
		self.heap_list = []
		self.current_size = 0

	#You will notice that an empty binary heap has a single zero as the first element 
	#of heap and that this zero is not used, but is there so that simple integer division can be used in later methods.


	#perc_up percolates up the newly added element and maintains the heap property

	#i//2 performs floor division
	def perc_up(self, i):
		while (i // 2)>0:
			#this while statement checks whether we have reached the root
			if self.heap_list[i] < self.heap_list[i // 2]:
				tmp = self.heap_list[i // 2]
				self.heap_list[i // 2] = self.heap_list[i]
				self.heap_list[i] = tmp
			i = i // 2

	def insert(self, k):
		self.heap_list.append(k)
		self.current_size = self.current_size + 1
		self.perc_up(self.current_size)

	#while deleting min element from heap we need these functions
	#perc_down and min_child in order to delete and maintain heap property. 
	def perc_down(self, i):
		while (i*2) <= self.current_size:
			minimum_child =  self.min_child(i)
			if self.heap_list[i] > self.heap_list[minimum_child]:
				tmp = self.heap_list[i]
				self.heap_list[i] = self.heap_list[minimum_child]
				self.heap_list[minimum_child] = tmp
			i = minimum_child

	def min_child(self, i):
		if (i * 2 + 1) > self.current_size:
			return i * 2
		else:
			if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
				return i * 2
			else:
				return i * 2 + 1

	def del_min(self):
		retval = self.heap_list[1]
		self.heap_list[1] = self.heap_list[self.current_size]
		self.current_size = self.current_size - 1
		self.heap_list.pop()
		self.perc_down(1)
		return retval

	def build_heap(self, alist):
		i = len(alist) // 2
		self.current_size = len(alist)
		self.heap_list = [0] + alist[:]
		while (i > 0):
			self.perc_down(i)
			i = i - 1


binary_heap = BinHeap()
list = map(int,raw_input().split())
binary_heap.build_heap(list)

print (binary_heap.heap_list)