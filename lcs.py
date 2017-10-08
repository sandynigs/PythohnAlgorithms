def lcs(x, y):
	m = len(x)
	n = len(y)
	c = [[0 for x in range(0,m+1)] for x in range(0,n+1)]
	for i in range(1,n+1):
		for j in range(1,m+1):
			if (y[i-1] == x[j-1]):
				c[i][j] = c[i-1][j-1] + 1
			else:
				c[i][j] = max(c[i-1][j], c[i][j-1])
	print ("length of longest common subsequence is", c[-1][-1])

x = input() #input string 
y = input() #input string 
c = lcs(x,y)
