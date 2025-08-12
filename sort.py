class Sort:
	def __init__(self, data:list, alg: str='quick'):
		self.data = data
		algorithms = {
            'quick': self.quick_sort,
            'merge': self.merge_sort,
            'bubble': self.bubble_sort
        }
		if alg not in algorithms:
			# raise ValueError(f"Unknown algorithm: {alg}")
			alg='quick'
		
		self.data=algorithms[alg](self.data)  

	
	def quick_sort(self):
		def partition(arr,low,high):
			pivot=arr[low]
			leftwall = low

			for i in range(low+1,high):
				if(arr[i]<pivot):
					temp = arr[leftwall]
					arr[leftwall]=arr[i]
					arr[i]=temp
					leftwall+=1
			temp = arr[leftwall]
			arr[leftwall]=arr[low]
			arr[low]=temp
			return(leftwall)
		# if low<high:
		# 	pivot_location=partition()
	def merge_sort(self,data):
		def merge(l,r):
			arr = list()
			while(l and r):
				if l[0]<r[0]:
					arr.append(l[0])
					l.pop(0)
				else:
					arr.append(r[0])
					r.pop(0)
			while l:
				arr.append(l[0])
				l.pop(0)
			while r:
				arr.append(r[0])
				r.pop(0)

			return 	arr
		

		size = len(data)
		if size < 2:
			return data		
		

		left = self.merge_sort(data[0:int(size/2)])
		right = self.merge_sort(data[int(size/2):size])
		m = merge(left,right)
		# print("Running merge sort on", m)
		return m

	def bubble_sort(self):
		print("Running bubble sort on", self.data)
if __name__=='__main__':
	unordered = [3,5,1,63,7,6,2,62,72,162,21]
	print(Sort(unordered,'merge').data)
