
Numbers = list(range(2000,3201))
Result= []
for Number in Numbers:
		D= Number % 7
		M= Number % 5 
		if D == 0 and M != 0:
			
			
			Result.append(Number)
	
print(Result)
