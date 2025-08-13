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

	
	def quick_sort(self,data):
		def quick( arr, low, high):

			def partition(arr,low,high):

				#Improve pivot choice
				pivot=arr[high]
				leftwall = low

				for i in range(low,high):
					if(arr[i]<pivot):
						temp = arr[leftwall]
						arr[leftwall]=arr[i]
						arr[i]=temp
						leftwall+=1

				temp = arr[leftwall]
				arr[leftwall]=arr[high]
				arr[high]=temp
				return(leftwall)
			
			if low<high:
				pivot_location=partition(arr,low,high)
				quick(arr, low, pivot_location-1)
				quick(arr,pivot_location+1,high)

			# print(arr)
			return arr
		return quick(data,0,len(data)-1)

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

	def bubble_sort(self,data):

		def bubble(arr,rightwall):
			if rightwall>0:
				for i in range(0, rightwall):
					if arr[i]>arr[i+1]:
						temp = arr[i+1]
						arr[i+1] = arr[i]
						arr[i] = temp
						print(arr)
				return bubble(arr,rightwall-1)
			
			return arr
		return bubble(self.data,len(self.data)-1)
		print("Running bubble sort on", self.data)


if __name__=='__main__':
	unordered = [3,5,1,63,7,6,2,62,72,162,21]
	#unordered = [3,5,1,63,7,6]
	print(Sort(unordered,'bubble').data)
