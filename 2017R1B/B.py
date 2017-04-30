import sys
sys.setrecursionlimit(2000)
for T in range(input()):
    N, R, O, Y, G, B, V=map(int,raw_input().split())
    # print N
    # print R, O, Y, G, B, V
    S=[R, O, Y, G, B, V]
    cnts={
    'R':R,
    'O':O,
    'Y':Y,
    'G':G,
    'B':B,
    'V':V,
    }
    nbs={
    'R':'YBG',
    'O':'VBG',
    'Y':'RVB',
    'G':'ORV',
    'B':'ORY',
    'V':'OYG',
    }
    # print cnts
    cs=sorted([(cnts[c],c) for c in cnts if cnts[c]],reverse=True)
    c=cs[0][1]
    path=[c]
    cnts[c]=cnts[c]-1
    def dfs(c,cnts,path):
        cs=sorted([(cnts[c],c) for c in cnts if cnts[c]],reverse=True)
        if len(cs)==0: return path
        if len(cs)==1: return False
        path+="{}{}".format(cs[0][1],cs[-1][1])
        cnts[cs[0][1]]=cnts[cs[0][1]]-1
        cnts[cs[-1][1]]=cnts[cs[-1][1]]-1
        
        #print len(path),
        for k in cnts:
            if cnts[k]>1:
                if sum([cnts[b] for b in nbs[k]])<cnts[k]-1: return False

        bs=sorted([(cnts[b],b) for b in nbs[c] if cnts[b]>0],reverse=True)
        # print c,path,bs,cnts
        if not bs:
            # print c,cnts,path
            if any(cnts.values()) or path[0]==path[-1]:
                return False
            else:
                return path
        maxcnt=bs[0][0]
        for cnt,b in bs:
            if cnt==maxcnt:
                cnts[b]=cnts[b]-1
                r=dfs(b,cnts,path+[b])
                if r: return r
                cnts[b]=cnts[b]+1
            else:
                break
        return False
        # c=bs[0][1]
        # cnts[c]=cnts[c]-1
        # path.append(c)
    path=dfs(c,cnts,[c])
    # # print cnts
    # def simple(R,Y,B):
    #     if R==0:
    #         if B==Y:
    #             print 'YB'*B
    #     else:
    #         return (R+abs(B-Y))%2==0
    # def s2(cnts):
    #     cs=sorted([(cnts[c],c) for c in cnts if cnts[c]],reverse=True)
    #     c=cs[0][1]
    #     path=c
    #     cnts[c]=cnts[c]-1
    #     while True:
    #         cs=sorted([(cnts[c],c) for c in cnts if cnts[c]],reverse=True)
    #         if len(cs)==0: return path
    #         if len(cs)==1: return False
    #         path+="{}{}".format(cs[0][1],cs[-1][1])
    #         cnts[cs[0][1]]=cnts[cs[0][1]]-1
    #         cnts[cs[-1][1]]=cnts[cs[-1][1]]-1

    path=s2(cnts)
    if not path:
        s='IMPOSSIBLE'
    else:
        # s="".join(path)
        s=path
    print "Case #{}: {}".format(T+1,s)
