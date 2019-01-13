
class Indices:
	def ind(lst1,ele):
		lst2=[]
		for j in range(len(lst1)):
			if ele==lst1[j]:
				lst2.append(j)
		print(lst2)
lst1=[]
str1=input("enter the values")
lst1=str1.split()
ele=input("enter the element to be searched")
a=Indices
a.ind(lst1,ele)