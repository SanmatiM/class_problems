lst1=[]
lst2=[]
n=int(input("enter number of elements in list"))
for i in range(n):
	lst1.extend(input("Enter input numbers"))
for num in lst1:
	if int(num)<5:
		lst2.append(num)

print(lst2)
