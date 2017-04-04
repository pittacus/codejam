import sys

# Round A APAC
# https://code.google.com/codejam/contest/3214486/dashboard

def A():
	LED={
#		  "ABCDEFG"
		0:"1111110",
		1:"0110000",
		2:"1101101",
		3:"1111001",
		4:"0110011",
		5:"1011011",
		6:"1011111",
		7:"1110000",
		8:"1111111",
		9:"1111011",
	}
	T=[
#		"UEBG" unknown, error, bad, good
		"0123",
		"1111",
		"2121",
		"3113",
	]
	M={n:map(int,list(LED[n])) for n in LED}
	T=[map(int,list(t)) for t in T]

	def solve(S):
		#print S
		s=set()
		for n in M:
			P=[0]*7
			for x,V in enumerate(S):
				t=((n-x)%10+10)%10
				Q=[x*2+y for x,y in zip(M[t],V)]
				P=[T[x][y] for x,y in zip(P,Q)]
				#print t,M[t],V,P
			if all([(p==2 or p==3 or p==0) for p in P]):
				Q=M[((t-1)%10+10)%10]
				for x,y in zip(P,Q):
					if x==0 and y!=0: return "ERROR!"
				v=[y if x==3  else 0 for x,y in zip(P,Q)]
				s.add("".join(map(str,v)))
		s=list(s)
		#if len(s)>1: print "DUP",s,
		return s[0] if len(s)==1 else "ERROR!"

	for n in range(input()):
		S=map(lambda x:map(int,list(x)),raw_input().split()[1:])
		#if n!=69-1: continue
		s=solve(S)
		print "Case #{}: {}".format(n+1,s)

def B():
	def rowsum(s):
		n=len(s)
		p=s
		p=[x for x in p if x>0]
		k=0
		while k<len(p)-1:
			if p[k]==p[k+1]:
				p[k]*=2
				p[k+1]=0
				k+=2
			else:
				k+=1
		p=[x for x in p if x>0]
		return p+[0]*(n-len(p))

	def solve(d,S):
		if d=="left":
			S=[rowsum(s) for s in S]
		elif d=="right":
			S=[rowsum(s[::-1])[::-1] for s in S]
		elif d=="up":
			S=zip(*[rowsum(s) for s in zip(*S)])
		elif d=="down":
			S=zip(*[rowsum(s[::-1])[::-1] for s in zip(*S)])
		return S

	for t in range(input()):
		n,d=raw_input().split()
		n=int(n)
		S=[map(int,raw_input().split()) for x in range(n)]
		#if n!=69-1: continue
		s=solve(d,S)
		print "Case #{}: \n{}".format(t+1,"\n".join(map(lambda x:" ".join(map(str,x)),s)))

def C():
	for t in range(input()):
		M=[[None]*10000 for x in range(10000)]
		S={}
		H=set()
		for n in range(input()):
			s,v=raw_input().split("=")
			x,y=s.split("+")
			v=int(v)
			if x not in S: S[x]=len(S)
			if y not in S: S[y]=len(S)
			a,b=S[x],S[y]
			M[a][b]=M[b][a]=v

			C=set()
			for (c,d) in H:
				if M[b][c] and not M[a][d]:
					M[d][a]=M[a][d]=M[a][b]+M[c][d]-M[b][c]
					C.add((a,d))

				if not M[b][c] and M[a][d]:
					M[b][c]=M[c][b]=M[a][b]+M[c][d]-M[a][d]
					C.add((b,c))

				if a==b and c==d and not M[a][c]:
					M[a][c]=M[c][a]=(M[a][a]+M[c][c])/2
					C.add((a,c))

			H.add((a,b))
			H.update(C)
			#print len(H)

		print "Case #{}: {}".format(t+1,"")
		for n in range(input()):
			s=raw_input()
			x,y=s.split("+")
			if x in S and y in S:
				v=M[S[x]][S[y]]
				if v: print "{}+{}={}".format(x,y,v)
		#break
def C2():
	for t in range(input()):
		M={}
		for n in range(input()):
			s,v=raw_input().split("=")
			x,y=s.split("+")
			v=int(v)
			if x not in M: M[x]={}
			if y not in M: M[y]={}
			M[x][y]=v
			M[y][x]=v

		S=set()
		def dfs(s,e,d,sum):
			global S
			if d==0: S=set()
			if s==e: return sum
			for x in M[s]:
				for y in M[x]:
					if y in S: continue
					S.add(y)
					r=dfs(y,e,d+2,sum-M[s][x]+M[x][y])
					if r: return r
			return []
		def solve(x,y):
			Q=[]
			V=set()
			for n in M[x]:
				Q.append((n,M[x][n]))
				V.add(n)
			while Q:
				(n,v)=Q.pop()
				if n==y: return [v]
				for n1 in M[n]:
					for n2 in M[n1]:
						if n2 not in V:
							Q.append((n2,v-M[n][n1]+M[n1][n2]))
							V.add(n2)
			return []
		print "Case #{}: {}".format(t+1,"")
		for n in range(input()):
			s=raw_input()
			x,y=s.split("+")
			if x not in M or y not in M: continue
			v=solve(x,y)
			if not v:
				v1=solve(x,x)
				if v1: v2=solve(y,y)
				if v1 and v2: v=[(v1[0]+v2[0])/2]
			if v: print "{}+{}={}".format(x,y,v[0])

def D():
	for t in range(input()):
		S=map(int,raw_input().split())
		N=S.pop(0)
		M=S.pop(0)
		C=[0]*32
		for s in S: C[s]+=1
		def solve(w,h):
			if w>h: w,h=h,w
			ks=[k for k in range(32) if (1<<k)<=w and C[k]]
			if not ks: return
			k=ks.pop()
			m=(1<<k)
			count=min(h//m,C[k])
			C[k]-=count
			solve(w-m,count*m)
			solve(w,h-count*m)
		count=0
		while any(C):
			solve(M,M)
			count+=1
		print "Case #{}: {}".format(t+1,count)
D()
