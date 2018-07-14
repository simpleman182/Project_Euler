def divide(n):
	lst = []
	for i in range(1,int(n/2)+1):
		if n % i == 0:
			lst.append(i)
	result = sum(lst)
	return result

lst = []

for i in range(0,28124):
	if i < divide(i) :
		lst.append(i)

result = [0]*28124
for x in range(0, len(lst)):
	for y in range(x,len(lst)):
		sums = lst[x] + lst[y]
		if (sums<=28123):
		    if (result[sums] == 0):
		    	result[sums] = sums

total = 0
for k in range(1,len(result)):
	if result[k] == 0:
		total += k

print total

