def chiahet(n):
	lst = []

	for i in range(1,n):
		if n % i == 0:
			lst.append(i)
	result = sum(lst)
	return result

lst = []	
for i in range(1,10000):
	temp = chiahet(i)
	if chiahet(temp) == i and temp != i:
		lst.append(i)

print (sum(lst))
