import sys

# Round B APAC
# https://code.google.com/codejam/contest/4214486/dashboard

def A():
	P=1000000007
	U=100+1

	M=[[0]*U for k in range(U)]
	M[1]=[1]*U
	for x in range(2,101):
		for y in range(x,101):
			M[x][y]=(M[x-1][y-1]+M[x][y-1])*x
			M[x][y]%=P
	#print M[2]
	#print M[3]
	for t in range(input()):
		x,y=map(int,raw_input().split())
		print "Case #{}: {}".format(t+1,M[x][y]%P)

A()
