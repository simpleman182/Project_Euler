def factorial(n):
	result = 1
	for i in range(1,n+1):
		result *= i
	return result

result = 0
temp = factorial(100)
temp = str(temp)
for i in temp:
	result += int(i)
print (result)
