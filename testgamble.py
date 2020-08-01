def uniq(input):# unique
    op=[]
    count=[]
    t=[]
    for x in input:
        if x.lower() not in t:
            op.append(x)
            t.append(x.lower())
            #count.append(input.count(x))
    return op#,count




l_unique=[]
def hii(n,l):
    str = ""
    str1 = ""
    l_uni = []
    print("reached here")
    print(l)
    for i in range(n):
        # l.append()
        l_uni.append(uniq(l[i]))
        # l=[]
    print(l_uni)
    for i in range(n):
        str = str + " ".join(l_uni[i]) + "\n"
        str1 = str1 + str
        str = ""
    return str1
n=int(input())
l=[]
for i in range(n):
    l.append(input().split(" "))

print(hii(n,l))




