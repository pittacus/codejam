import sys

# Qualification Round Africa 2010
# https://code.google.com/codejam/contest/351101/dashboard#s=p0

def A():
	def solve(C,P):
		M=[0]*2000
		for x,p in enumerate(P):
			x+=1
			if p>=C: continue
			if M[C-p]: return sorted([M[C-p],x])
			M[p]=x

	N=int(input())
	for n in range(N):
		C=int(input())
		L=int(input())
		P=map(int,sys.stdin.readline().strip().split())
		x,y=solve(C,P)
		print "Case #{}: {} {}".format(n+1,x,y)
def B():
	def solve(P):
		return reversed(P)

	N=int(input())
	for n in range(N):
		P=sys.stdin.readline().strip().split()
		P=solve(P)
		print "Case #{}: {}".format(n+1," ".join(P))
def C():
	def solve(P):
		keymap={
		2:'abc',
		3:'def',
		4:'ghi',
		5:'jkl',
		6:'mno',
		7:'pqrs',
		8:'tuv',
		9:'wxyz',
		0:' ',
		}
		M={}
		for k in keymap:
			for n,c in enumerate(keymap[k]):
				M[c]=str(k)*(n+1)
		s=' '
		for c in P:
			if M[c][0]==s[-1]: s+=' '
			s+=M[c]
		return s[1:]
	N=int(input())
	for n in range(N):
		P=sys.stdin.readline()[:-1]
		s=solve(P)
		print "Case #{}: {}".format(n+1,s)
