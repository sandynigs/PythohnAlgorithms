def greedy_knapsack(m,w,p,n):
	#devise algorithm to store objects in reverse order of p/w
	greedy_list = []
	for i in range(0,n):
		greedy_list.append(((float(p[i])/w[i]),i))
	greedy_list.sort(reverse = True)
	print (greedy_list)

	P = 0

	for i in greedy_list:
		print("w[i[1]] is",w[i[1]])
		print("p[i[1]] is",p[i[1]])
		if (m>0 and w[i[1]]<=m):
			m = m - w[i[1]]
			P = P + p[i[1]]
		else:
			break
	print("P is",P)
	if (m>0):
		P = P + (p[i[1]] * (float(m)/w[i[1]]))

	print ("maximum profit is",P)

print("total capacity of sack")
m = int(input())
print("list of weights")
w = list(map(int,input().split()))
print("respective list of profits")
p = list(map(int,input().split()))
n = len(w)
greedy_knapsack(m,w,p,n)