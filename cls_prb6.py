d=dict()
name=[]
usn=[]
for n in range(3):
	n=input("Enter name")
	name.append(n)
	u=input("enter usn")
	usn.append(u)
d=dict(zip(usn,name))
print(d)