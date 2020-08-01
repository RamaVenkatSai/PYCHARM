#from FixTk import v
#from pickletools import i
from string import lower
def uniq(input):
    op=[]
    count=[]
    t=[]
    for x in input:
        if x.lower() not in t:
            op.append(x)
            t.append(x.lower())
            count.append(input.count(x))
    return op,count
n=int(input())
i=0
str=[]
v=[]
lm=[]
cout=[]
for  i in range(0,n):
    v[i] = input().split(" ")

    lm[i] = []
    cout[i] = []
    str[i].append()
    v[i] = str[i].split(" ")
    lm[i], cout[i] = uniq(v[i])
    str[i]=" ".join(lm[i])
    print(str[i])

#mylist = list(dict.fromkeys(mylist))
#print(mylist)
#k=dict.fromkeys(mylist)
#print(k)



