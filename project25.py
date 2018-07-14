a = 1 
b = 1
count = 2
while len(str(b)) <= 1000:
	a, b = b, a+b
	count += 1
	print (b, count, len(str(b)))