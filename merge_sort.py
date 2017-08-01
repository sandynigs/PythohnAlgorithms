import math
def mergeSort(array,p,r):
	if p<r:
		q = math.floor((p+r)/2)
		mergeSort(array,p,q)
		mergeSort(array,q+1,r)
		merge(array,p,q,r)
def merge(array,l,m,n):
	n1 = m-l+1
	n2 = n-m
	L = [0]*(n1+1)
	R = [0]*(n2+1)
	for i in range(0,n1):
		L[i] = array[l+i]
	for j in range(0,n2):
		R[j] = array[m+1+j]
	L[n1]=math.inf
	R[n2]=math.inf
	i = 0     
	j = 0     

	for k in range(l,n+1):
		if (L[i]<=R[j]):
			array[k] = L[i]
			i += 1
		else:
			array[k] = R[j]
			j += 1

array = list(map(int,input().split()))
n = len(array)
mergeSort(array,0,n-1)
print (array)