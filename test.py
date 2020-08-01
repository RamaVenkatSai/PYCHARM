txt = "           ,,, banana          "

x = txt.rstrip(" ,bna")  #lstrip and rstrip are used to delete white spaces and tabspaces
# and when u give a character like bna all alphabets of b a n will be removed
print("lstrip:")
print(x)
myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)
myDict = {"name": "John", "country": "Norway","kk":"manhole"}
mySeparator = "TEST"

x = mySeparator.join(myDict) # it joins right to left order

print(x)
txt = "Hello, welcome to my world."

x = txt.index("l")

print(x)
x =txt.split(" ")
print(x)

man="#".join(x)
print(man)