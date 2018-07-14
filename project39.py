def triangle(p):
	count = 0
	for a in range(p,1,-1):
		for b in range((p-a),a,-1):
			c = p - a - b
			if a**2 + b**2 - c**2 == 0 and (a+b+c)==p:
			    count +=1
	return (count)

result = 0
total = 0
for i in range(12,1001):
	print (i)
	if triangle(i) > result:
		result = triangle(i)
		total = i
print (total)