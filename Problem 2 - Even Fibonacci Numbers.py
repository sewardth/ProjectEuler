fibs = [1,2]

y=0
while y < 4000000:
	y = sum(fibs[-2:])
	fibs.append(y)

total = sum([x for x in fibs if x % 2 ==0])
print total
