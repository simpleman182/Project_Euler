result = []
for x in range(2,354294):
	total = 0
	for i in str(x):
		total += int(i) ** 5
	if total == x:
		print (x)
		result.append(x)
print (sum(result))



