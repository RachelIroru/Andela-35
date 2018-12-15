
marks = [23,4,5,6,64,90,67,98,45,23,67,78,89]
Greater=[]
Less=[]
for mark in marks:
		if mark <= 50:
			Less.append(mark)
		else:
			Greater.append(mark)
	
			if mark >=90 and  mark <=100:
				print("Execellent")
			elif mark >=70 and mark <=70:
				print("Very Good")
			elif mark >=60 and mark <=69:
				print("Good")
			elif mark >=40 and mark <=59:
				print("Poor")
			elif mark >=20 and mark <=39:
				print("Very Poor")
			else:
				print("Repeat")
				
print("\nList numbers:\n")
print(Less)
print(Greater)
